# Password Manager

This Python program serves as a simple password manager that allows users to securely store and retrieve usernames and passwords. It utilizes the cryptography library for encryption and decryption of sensitive information.

## Features

- Encryption of stored usernames and passwords for enhanced security.
- Master password authentication to control access to the password manager.
- Options to add, view, and quit the password manager.

## Usage

1. **Adding Usernames and Passwords**:
   - Choose the 'add' option and enter the desired username and password.
   - The provided credentials will be securely stored in the password manager.

2. **Viewing Usernames and Passwords**:
   - Select the 'read' option and enter the master password.
   - Upon successful authentication, the stored usernames and passwords will be displayed.

3. **Quitting the Password Manager**:
   - To exit the program, choose the 'q' option.

## Implementation Details

- The program encrypts the stored usernames and passwords using the Fernet symmetric encryption scheme provided by the cryptography library.
- A master password is set to control access to the password manager. Only authorized users with the correct master password can access the stored credentials.
- User input and interactions are handled through the command-line interface (CLI) with clear prompts and error messages to guide users.

## Setup and Requirements

- Python 3.x
- Install the cryptography library using pip: `pip install cryptography`

## Note

- It's important to remember the master password as it grants access to all stored credentials.
- Ensure to keep the encrypted file (e.g., 'MyFile.txt.encrypted') in a secure location.

