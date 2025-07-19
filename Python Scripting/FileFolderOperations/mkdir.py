from pathlib import Path

folder = Path(r"C:\DEVELOPMENT\PYTHON\Python Scripting\FileFolderOperations\GeneratedReports")

# Create the folder if it doesn't exist
folder.mkdir(parents=True, exist_ok=True)

print("✅ Folder is ready:", folder)
