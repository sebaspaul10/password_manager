# Import the Fernet class from the cryptography library
from cryptography.fernet import Fernet

# Define a function to generate a key for encryption
def generate_key():
    return Fernet.generate_key()

# Define a function to encrypt a file
def encrypt_file(file_path, key):
    # Open the file in binary read mode
    with open(file_path, 'rb') as f:
        # Read the contents of the file
        data = f.read()

    # Create a Fernet cipher instance with the provided key
    cipher = Fernet(key)
    # Encrypt the data read from the file
    encrypted_data = cipher.encrypt(data)

    # Append '.encrypted' to the original file path to create the encrypted file path
    encrypted_file_path = file_path + '.encrypted'
    # Open the encrypted file in binary write mode
    with open(encrypted_file_path, 'wb') as f:
        # Write the encrypted data to the encrypted file
        f.write(encrypted_data)
    
    # Return the path of the encrypted file
    return encrypted_file_path

# Define a function to display the contents of an encrypted file
def display_encrypted_file(file_path):
    # Open the encrypted file in binary read mode
    with open(file_path, 'rb') as f:
        # Read the contents of the encrypted file
        encrypted_data = f.read()
    # Print the hexadecimal representation of the encrypted data
    print(encrypted_data.hex())

# Define a function to write a username and password to a file
def file_user_pass(x, y):
    # Open the file in append mode
    f = open ("MyFile.txt", "a")
    # Write the username and password to the file
    f.write ("Username : " + x + " | " + "Password : " + y + "\n")
    # Close the file
    f.close()

# Define a function to read and print usernames and passwords from a file
def read_file_user_pass():
    # Open the file in read mode
    f = open ("MyFile.txt", "r")
    # Iterate over each line in the file
    for x in f:
        # Print each line
        print(x)
    # Close the file
    f.close()

# Generate a key for encryption
key = generate_key()

# Encrypt a file and get the name of the encrypted file
encrypted_file_path = encrypt_file('MyFile.txt', key)

# Set the master password
Master_password = "kankudai"

# Prompt the user for their name
while True:
    name = input ("Enter your name : ")
    # Check if the name matches the authorized user
    if not (name.lower() == "sebastien"):
        print ("Error, you can't access the password manager, try again !")
        continue
    else:
        break

# Welcome message
print (f"Welcome {name} !")

# Main menu loop
while True:
    # Prompt the user for their choice
    choice = input ("Please enter 'add' to add usernames and passwords, 'read' to access them, or 'q' to quit :")
    if choice.lower() == "add":
        # Prompt the user for a username and password and write them to the file
        user_name = input ("Enter user name : ")
        password = input ("Enter password : ")
        file_user_pass(user_name, password)
        continue
    elif choice.lower() == "read":
        # Access control loop
        while True:
            password = input ("Please enter the master password : ")
            # Check if the entered password matches the master password
            if password.lower() == Master_password:
                # Read and print usernames and passwords from the file
                read_file_user_pass()
                break
            if not (password.lower() == Master_password):
                # Display an error message and show the encrypted data
                print ("Error in the password !!!")
                display_encrypted_file(encrypted_file_path)
                continue 
            break
        continue
    elif choice.lower() == "q":
        # Quit the program
        break
    else:
        # Display an error message for invalid input
        print ("Error !")
        continue 
