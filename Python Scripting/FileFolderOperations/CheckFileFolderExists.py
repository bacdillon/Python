import os

folder_path = r"C:\DEVELOPMENT\PYTHON\Python Scripting\FileFolderOperations\GeneratedReports"
file_path = r"C:\DEVELOPMENT\PYTHON\Python Scripting\File & Folder Operations\data.xlsx"

# Check if folder exists
if os.path.isdir(folder_path):
    print("✅ Folder exists.")
else:
    print("❌ Folder does not exist.")

# Check if file exists
if os.path.isfile(file_path):
    print("✅ File exists.")
else:
    print("❌ File not found.")
