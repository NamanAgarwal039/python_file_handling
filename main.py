from pathlib import Path
import os

def readdirectory():
    path = Path('')
    items = list(path.rglob('*'))
    for i , items in  enumerate(items):
        print(f"{i+1} : {items}")
        
#Creating a new file
def createfile():
    try:
        readdirectory()
        name =input("Please tell your file name :- ")
        p= Path(name)
        if not p.exists():
            with open(p,'w') as fs:
                data= input("Enter the data which you want to enter in the file : ")
                fs.write(data)
    except Exception as err:
        print(f"An error occured as {err}")
print("FILE CREATED SUCESSFULLY ")



#reading a file which already exists
def readfile():
    try:
        readdirectory()
        name = input("which file you want to read :-")
        p= Path(name)
        if p.exists() and p.is_file():
            with open(p,'r') as fs:
                data = fs.read()
                print(data)


                print("FILE READED SUCCESSFULLY")
        else:
            print("File doesn't exists")
    except Exception as err:
        print(f"An Error occured as {err} ")



def updatefile():
    try:
        readdirectory()
        name = input("tell which file do you want to update ")
        p = Path(name)
        if p.exists() and p.is_file():

            print("press 1 for change the name of the file :- ")
            print("press 2 for override the data of the file :- ")
            print("press 1 for append some content in your file :- ")


            response = int(input("Enter your response :- "))

            if response ==1:
                name2= input("Tell your new file name :- ")
                p2 = Path(name2)
                p.rename(p2) 

            if response ==2:
                with open(p,'w') as fs:
                    data = input("Tell what do you want to write :-")
                    fs.write(data)
            if response ==3:
                with open(p,'a') as fs:
                    data=input("enter the data which you want to append :-")
                    fs.write(" "+data)
    except Exception as err:
        print(f"An error occurs as {err}")       

def deletefile():
    try:
        readdirectory()
        name= input("which file you want to delete :- ")
        p = Path(name)

        if p.exists() and p.is_file():
            os.remove(p)

            print("File removed sucessfully")

        else:
            print("No such file exists")
    except Exception as err:
        print(f"Error occurs as {err}")





print("Press 1 for creating a file")
print("Press 2 for reading  a file")
print("Press 3 for  update  a file")
print("Press 4 for deletion a file")




check = int(input("Please tell your response :- "))
if check ==1:
    createfile()

if check ==2:
    readfile()

if check == 3:
    updatefile()

if check ==4:
    deletefile()