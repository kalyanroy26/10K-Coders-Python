import os

def searchFile():
    folder = input("enter folder name: ")
    file = input("enter file name: ")
    if not os.path.isdir(folder):
        os.mkdir(folder)
        print(f"{folder} is created")
        path = os.path.join(folder,file)

    with open(path,"x") as file:
        file.write("")
        print(f"empty file is created at {path}")

searchFile()



        

