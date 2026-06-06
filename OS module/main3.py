#LIST
import os
folders=os.listdir("OS module/FIRST FOLDER")
#print(folders)
for folder in folders:
    print(folder)
    print(os.listdir(f"OS module/FIRST FOLDER/{folder}"))
