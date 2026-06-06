#Os module
import os

if(not os.path.exists("FIRST FOLDER")):
    os.mkdir("OS module/FIRST FOLDER")
for i in range(0,1000):
    os.mkdir(f"OS module/FIRST FOLDER/i_hate_karela{i+1}")
#Creates 100 folder named i hate karela