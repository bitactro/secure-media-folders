# Secure Media Folders

## Overview

`secure-media-folders` is a **GUI-based, cross-platform personal utility tool** designed to help users **encrypt and decrypt media folders** (and nested subfolders) using **password-based encryption**. It is intended to **secure your images and videos** without compressing them. Users only need to remember the password used for encryption to decrypt the folders.

This project is perfect for general users seeking privacy, as well as for senior engineers and architects reviewing a lightweight, secure, personal utility.

---

## Key Features

* 🖥️ **GUI-based Interface:** User-friendly graphical interface for easy folder selection
* 🔒 **Secure Folder Encryption:** Protect your images and videos using strong encryption
* 📁 **Recursive Nested Folder Support:** Automatically encrypts/decrypts all subfolders
* 🔑 **Password-only Decryption:** No keys or files needed — just remember your password
* 🚫 **Non-compression of Media:** Media files remain in their original format and size
* 💻 **Cross-Platform:** Available builds for Windows (.exe), Debian (.deb), and RHEL (.rpm)
* 📦 **Releases Available:** Pre-built releases can be found [here](https://github.com/bitactro/secure-media-folders/releases)

---

## Installation & Setup

### 1. Download Pre-built Builds

* **Windows:** `.exe` file
* **Debian:** `.deb` package
* **RHEL/CentOS:** `.rpm` package

Releases available here: [Releases Page](https://github.com/bitactro/secure-media-folders/releases)

### 2. Optional: Install from Source

```bash
git clone https://github.com/bitactro/secure-media-folders.git
cd secure-media-folders

# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

---

## Usage

### Launch GUI

* **Windows:** Double-click the `.exe` file from the release build
* **Debian/RHEL/Linux:** Launch the GUI from your applications menu or via terminal command (if installed from `.deb`/`.rpm`)

### Encrypt a Folder

1. Open the application
2. Select the folder you want to encrypt
3. Enter a password
4. Click **Encrypt**

### Decrypt a Folder

1. Open the application
2. Select the encrypted folder
3. Enter the password used for encryption
4. Click **Decrypt**

### Notes

* Ensure you **remember your password**; encrypted folders cannot be recovered without it
* The tool **does not compress media files**, preserving original quality

---

## Architecture Diagram

```text
[User Folder] --> [GUI Application Encryption] --> [Encrypted Folder]
[Encrypted Folder] --> [GUI Application Decryption] --> [Original Folder]
```

* Input Folder: Your media folder with images/videos
* GUI App: Handles encryption and decryption recursively
* Output Folder: Encrypted or decrypted version of the folder

---

## Roadmap / Future Improvements

* 🌐 Enhance GUI with drag-and-drop support
* 📱 Mobile app support for Android/iOS
* ☁️ Cloud storage integration (e.g., Google Drive, Dropbox)
* 🔐 Multi-user encryption support

---

## License

This project is licensed under the **MIT License**.

```
MIT License

Copyright (c) 2025 Ankit Mishra

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

---

## Author

**Ankit Mishra**
Personal Utility App Developer • Open Source Contributor
