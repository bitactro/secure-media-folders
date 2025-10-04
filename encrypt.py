# update this according to your password.
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


def encrypt_file(key, in_filename, out_filename=None, chunksize=64 * 1024):
    hashed_key = hashlib.sha256(key.encode("utf-8")).digest()
    """ Encrypts a file using AES (CBC mode) with the given key.
        key:
            The encryption key - a string that must be either 16, 24 or 32 bytes long.
        in_filename:
            Name of the input file
        out_filename:
            If None, '<in_filename>.enc' will be used.
        chunksize:
            Sets the size of the chunk which the function uses to read and encrypt the file. Larger chunk
            sizes can be faster for some files and machines. chunksize must be divisible by 16.
    """
    if not out_filename:
        last_6_hex = hashed_key.hex()[-10:]
        out_filename = in_filename + last_6_hex + ".enc"

    iv = os.urandom(16)
    encryptor = AES.new(hashed_key, AES.MODE_CBC, iv)
    filesize = os.path.getsize(in_filename)

    with open(in_filename, "rb") as infile:
        with open(out_filename, "wb") as outfile:
            outfile.write(struct.pack("<Q", filesize))
            outfile.write(iv)

            while True:
                chunk = infile.read(chunksize)
                if len(chunk) == 0:
                    break
                elif len(chunk) % 16 != 0:
                    chunk += b" " * (16 - len(chunk) % 16)

                outfile.write(encryptor.encrypt(chunk))
    return True


def encryptAll(key, target_dir=None):
    base = target_dir if target_dir else base_dir
    success = False
    try:
        for root, dirs, files in os.walk(base, topdown=True):
            for file in files:
                if (
                    file.endswith(".jpeg")
                    or file.endswith(".jpg")
                    or file.endswith(".png")
                    or file.endswith(".mp4")
                    or file.endswith(".JPG")
                    or file.endswith(".PNG")
                    or file.endswith(".JPEG")
                ):
                    result = encrypt_file(key, os.path.join(root, file))
                    if result:
                        success = True
                        os.remove(os.path.join(root, file))
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")
        return False
    if success:
        messagebox.showinfo("Success", "Files encrypted successfully!")
        return True
    else:
        messagebox.showinfo("Info", "No files to encrypt.")
        return False
