import os
import shutil

file = ["1", "file", "File", "f"]
directory = ["2", "dir", "Directory", "directory", "folder", "Folder", "d"]

select = input("Select\n (1) File,\n (2) directory\n ")

if select in file:
    file_path = input("File Path: ").replace('\\', '/')
    if os.path.exists(file_path):
        os.remove(file_path)
    else:
        print("The file does not exist, please check again")

elif select in directory:
    dir_path = input("Directory Path: ").replace('\\', '/')
    if os.path.exists(dir_path):
        shutil.rmtree(dir_path)
    else:
        print("The directory does not exist, please check again")
else:
    print("Please check the value you selected again.")

    