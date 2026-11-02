from pathlib import Path
import os
import shutil

def create_folder():
    name = input("Tell your folder name:- ")
    p = Path(name)

    if p.exists():
        print("this folder name already exist please try again ")
        create_folder()
    else:
        p.mkdir()
        print("folder created successfully !")

def read_folder():
    p = Path("")
    names = list(p.rglob("*"))
    return names

def update_folder():
    names = read_folder()
    for i in names:
        i = str(i) 
        p = Path(i)
        if p.is_dir():
            print(i)
    name = input("which folder you want to update:- ")
    old_p = Path(name)

    if old_p.exists():
        new_name = input("Tell new folder name:- ")
        new_p = Path(new_name)
        old_p.rename(new_p)
        print("folder name changed successfully ")
    else:
        print("no such folder exist please try again ")
        update_folder()



def delete_folder():
    name = input("Tell your folder name:- ")
    p = Path(name)

    if not p.exists() or not p.is_dir():
        print("This folder does not exist. Please try again.")
        delete_folder()
    else:
        shutil.rmtree(p)
        print("Folder deleted successfully!")

def create_file():
    name = input("Tell your file name with extension ")
    p = Path(name)
    if p.exists():
        print("file already exists please try again ")
        create_file()
    else:    
        with open(p,"w") as file:
            data = input("Enter what you want to write : ")
            file.write(data)
            print("successfully created")

def read_file():
    name = input("Tell your file name with extension ")
    p = Path(name)
    if p.exists() and p.is_file():
        with open(p,"r") as file:
            data = file.read()
            print("\n\n\nYour file data is\n\n\n")
            print(data)

def delete_file():
    name = input("Tell your file name with extension ")
    p = Path(name)
    if p.exists() and p.is_file():
        os.remove(p)
        print("file deleted successfully ")
    else:
        print("No such file exist please try again")
        delete_file()

        
def update_file():
    names = read_folder()
    for i in names:
        i = str(i)
        p = Path(i)
        if p.is_file():
            print(i)

    name = input("which file you want to update :- ")
    p = Path(name)

    if p.exists() and p.is_file():
        print("press 1 to change the file name ")
        print("press 2 to overwrite the file ")
        print("press 3 to append something in your file ")

        check = int(input("Tell your output :- "))

        if check == 1:
            new_name = input("Tell the new name :- ")
            new_p = Path(new_name)
            p.rename(new_p)

        elif check == 2:
            with open(p,'w') as file:
                data = input("what do you want to overwrite:- ")
                file.write(data)
                print("overwritten successfully ")

        elif check == 3:
            with open(p,'a') as file:
                data = input("what do you want to append:- ")
                file.write(" "+ data)
                print("appended successfully ")
            

    else:
        print("no such file exists please try again ")
        update_file()




print("press 1 - for creating a folder")
print("press 2 - for reading a folder")
print("press 3 - for updating a folder")
print("press 4 - for deleting a folder")
print("press 5 - for creating a file")
print("press 6 - for reading a file")
print("press 7 - for updating a file")
print("press 8 - for deleting a file")

res = int(input("Tell your response:- "))

if res == 1:
    create_folder()

if res == 2:
    read_folder()

if res == 3:
    update_folder()

if res == 4:
    delete_folder()

if res == 5:
    create_file()

if res == 6:
    read_file()

if res == 7:
    update_file()

if res == 8:
    delete_file()