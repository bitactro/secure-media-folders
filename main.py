import os
import tkinter as tk
from tkinter import filedialog, messagebox, ttk

from decrypt import decryptAll
from encrypt import encryptAll


def select_folder():
    folder_path = filedialog.askdirectory()
    if folder_path:
        folder_var.set(folder_path)


def start_process():
    key = password_var.get()
    folder = folder_var.get()
    action = action_var.get()

    if not folder:
        messagebox.showerror("Error", "Please select a folder")
        return
    if not key:
        messagebox.showerror("Error", "Please enter password")
        return

    os.chdir(folder)
    try:
        if action == "Encrypt":
            encryptAll(key, target_dir=folder)
        else:
            decryptAll(key, target_dir=folder)
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")


# ----- GUI Setup -----
root = tk.Tk()
root.title("🔒 Secure Media Folder Encryptor")
root.geometry("500x250")
root.resizable(False, False)
root.configure(bg="#1e1e2f")

# Styles
style = ttk.Style()
style.theme_use("clam")
style.configure("TButton", font=("Helvetica", 11), padding=6)
style.configure(
    "TLabel", background="#1e1e2f", foreground="#ffffff", font=("Helvetica", 11)
)
style.configure("TEntry", font=("Helvetica", 11))
style.configure("TOptionMenu", font=("Helvetica", 11))

# Variables
folder_var = tk.StringVar()
password_var = tk.StringVar()
action_var = tk.StringVar(value="Encrypt")

# ----- Layout -----
frame = tk.Frame(root, bg="#1e1e2f", padx=20, pady=20)
frame.pack(fill="both", expand=True)

# Folder
tk.Label(frame, text="Select Folder:").grid(row=0, column=0, sticky="w")
folder_entry = ttk.Entry(frame, textvariable=folder_var, width=35)
folder_entry.grid(row=0, column=1, padx=5, pady=5)
ttk.Button(frame, text="Browse", command=select_folder).grid(row=0, column=2, padx=5)

# Password
tk.Label(frame, text="Password:").grid(row=1, column=0, sticky="w", pady=10)
ttk.Entry(frame, textvariable=password_var, show="*").grid(
    row=1, column=1, columnspan=2, sticky="we", padx=5
)

# Action
tk.Label(frame, text="Action:").grid(row=2, column=0, sticky="w", pady=10)
ttk.OptionMenu(frame, action_var, "Encrypt", "Encrypt", "Decrypt").grid(
    row=2, column=1, sticky="w", padx=5
)

# Start button
start_btn = ttk.Button(frame, text="Start", command=start_process)
start_btn.grid(row=3, column=0, columnspan=3, pady=20)

# Footer
tk.Label(
    frame,
    text="© 2025 Secure Media Tools",
    font=("Helvetica", 9),
    fg="#aaaaaa",
    bg="#1e1e2f",
).grid(row=4, column=0, columnspan=3, pady=5)

root.mainloop()
