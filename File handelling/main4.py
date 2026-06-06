"""
File Opening Modes in Python:

1. 'r' (Read)
   - Purpose: Opens the file for reading only.
   - File Position: The file pointer is positioned at the beginning of the file.
   - File Requirement: The file must exist. If it doesn't, an error (FileNotFoundError) is raised.

2. 'r+' (Read and Write)
   - Purpose: Opens the file for both reading and writing.
   - File Position: The file pointer is positioned at the beginning of the file.
   - File Requirement: The file must exist. If it doesn't, an error (FileNotFoundError) is raised.

3. 'w' (Write)
   - Purpose: Opens the file for writing only.
   - File Position: The file pointer is positioned at the beginning of the file.
   - File Effect: If the file already exists, it is truncated (i.e., its content is deleted). If the file does not exist, it is created.

4. 'w+' (Read and Write)
   - Purpose: Opens the file for both reading and writing.
   - File Position: The file pointer is positioned at the beginning of the file.
   - File Effect: If the file already exists, it is truncated. If the file does not exist, it is created.

5. 'a' (Append)
   - Purpose: Opens the file for writing only.
   - File Position: The file pointer is positioned at the end of the file.
   - File Effect: If the file already exists, data is appended to the end. If the file does not exist, it is created. Writes to the file will always occur at the end, regardless of file pointer movements.

6. 'a+' (Read and Append)
   - Purpose: Opens the file for both reading and writing.
   - File Position: The file pointer is positioned at the end of the file.
   - File Effect: If the file already exists, data is appended to the end. If the file does not exist, it is created. Reads can occur from anywhere in the file, but writes will always be appended to the end of the file.
"""
f=open('demo.txt','r+')
f.write("abc")#abc suru mai overwrite handyo
# print(f.read())
f.close()

