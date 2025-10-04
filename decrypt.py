import hashlib
import os
import struct
import sys
from tkinter import messagebox

from Crypto.Cipher import AES


def get_base_dir():
    if getattr(sys, "frozen", False):  # running as exe
        return os.path.dirname(os.path.abspath(sys.argv[0]))
    else:  # running as script
        return os.path.dirname(os.path.abspath(__file__))


base_dir = get_base_dir()


def decrypt_file(key, in_filename, out_filename=None, chunksize=24 * 1024):
    hashed_key = hashlib.sha256(key.encode("utf-8")).digest()
    last_6_hex = hashed_key.hex()[-10:]
    last_6 = in_filename[-14:-4]  # 10 = 6 (hex) + 4 (.enc)
    if last_6 != last_6_hex:
        return "EncryptionKeyMismatch"
    if not out_filename:
        out_filename = os.path.splitext(in_filename)[0]
        # Remove last 6 characters from out_filename
        out_filename = out_filename[:-10]

    with open(in_filename, "rb") as infile:
        origsize = struct.unpack("<Q", infile.read(struct.calcsize("Q")))[0]
        iv = infile.read(16)
        decryptor = AES.new(hashed_key, AES.MODE_CBC, iv)

        with open(out_filename, "wb") as outfile:
            while True:
                chunk = infile.read(chunksize)
                if len(chunk) == 0:
                    break
                outfile.write(decryptor.decrypt(chunk))

            outfile.truncate(origsize)
    return True


def decryptAll(key, target_dir=None):
    base = target_dir if target_dir else base_dir
    success = False
    encryptionKeyMisMatch = False
    try:
        for root, dirs, files in os.walk(base, topdown=True):
            for file in files:
                if file.endswith(".enc"):
                    result = decrypt_file(key, os.path.join(root, file))
                    if result == "EncryptionKeyMismatch":
                        encryptionKeyMisMatch = True
                        print("Decryption key does not match the encryption key.")
                        break
                    if result:
                        success = True
                        os.remove(os.path.join(root, file))
            if encryptionKeyMisMatch:
                break
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")
        return False

    if encryptionKeyMisMatch:
        messagebox.showinfo(
            "Error", "Decryption key does not match the encryption key."
        )
        return False
    if success:
        messagebox.showinfo("Success", "Files decrypted successfully!")
        return True
    else:
        messagebox.showinfo("Info", "No files to decrypt.")
        return False
