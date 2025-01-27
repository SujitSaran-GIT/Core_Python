# write a python program to print the contents of a directory using the os module. Search online for the function which does that

import os

# Specify the directory you want to list
directory = 'D:\PYTHON\CORE PYTHON'

try:
    # List all files and directories in the specified directory
    contents = os.listdir(directory)
    
    print(f"Contents of '{directory}':")
    for item in contents:
        print(item)
except FileNotFoundError:
    print(f"The directory '{directory}' does not exist.")
except PermissionError:
    print(f"Permission denied to access '{directory}'.")

# Explanation of this code
"""
Explanation:
import os: Imports the os module, which provides functions for interacting with the operating system.

directory = '/path/to/directory': Specifies the directory path you want to list the contents of. Replace '/path/to/directory' with the actual path of the directory.

os.listdir(directory): Returns a list of the names of the entries in the specified directory. This list includes both files and subdirectories.

try...except Block:

FileNotFoundError: Catches the error if the specified directory does not exist.
PermissionError: Catches the error if the program does not have permission to access the directory.
for item in contents:: Loops through the list of contents and prints each item.

Example Usage:
If you want to list the contents of your home directory, you could modify the directory variable like this:

python
Copy code
directory = '/home/your_username'  # On Linux or macOS
# or
directory = 'C:\\Users\\your_username'  # On Windows
This program will print the names of all files and subdirectories in the specified directory.

"""