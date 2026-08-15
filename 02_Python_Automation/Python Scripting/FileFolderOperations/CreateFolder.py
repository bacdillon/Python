import os

folder_path = r"C:\DEVELOPMENT\PYTHON\Python Scripting\FileFolderOperations\GeneratedReports"

# Create the folder if it doesn't exist
if not os.path.exists(folder_path):
    os.makedirs(folder_path)
    print("Folder created.")
else:
    print("Folder already exists.")
