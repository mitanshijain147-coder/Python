"""
FILES
x -> This mode will only create a file and if already exists we will get an erroe back.
w -> Agar file exist nhi kar rhi hai so this mode will create one and insert the content inside the file.
a
r
"""
# Mode 1 : x -> Just to create the file
#open("Garba.txt","x")

# Mode 2 : w -> If there is any content inside the file so the new one will replace the old one.
file = open("Garba.txt","w")
file.write("Kehlo garba khub khelo din raat khelo")


# Mode 3 : a -> add the text at the last.
file = open("Garba.txt", "a")
file.write("\nThis message is newly added")

# Mode 4 : r -> read the content inside the file. 
file = open("Garba.txt","r")
print(file.read())
file.close()

# Using this syntax file automatically open hogi aur close hogi
with open("sample.txt","w") as file:
    file.write("This is new file")

"""
FOLDER
mkdir -> to create a new folder or directory
rmdir -> to remove any folder/ directory
"""
import os
os.mkdir("Hello")

# CRUD - CREATE, READ, UPDATE, DELETE
os.remove("Garba.txt")
print("Press 1 for Creating a new Folder")
print("Press 2 for Reading any Folder" )
print("Press 3 for Updating ant folder")
print("Press 4 for Deleting any folder")
print("Press 5 - for creating a file")
print("Press 6 - for reading a file")
print("Press 7 - for updating a file")
print("Press 8 - for deleting a file")