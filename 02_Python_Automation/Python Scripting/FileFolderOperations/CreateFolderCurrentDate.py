from pathlib import Path
from datetime import datetime
import getpass

# Get current system username
username = getpass.getuser()

# Get current timestamp in YYYYMMDD_HHMMSS format
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

# Build folder name: e.g., Reports_Alfred_20250716_084500
folder_name = f"Reports_{username}_{timestamp}"

# Set base directory (optional — can be absolute path)
base_dir = Path("C:\DEVELOPMENT\PYTHON\Python Scripting\FileFolderOperations\GeneratedReports")

# Combine into full path
full_path = base_dir / folder_name

# Create folder
full_path.mkdir(parents=True, exist_ok=True)

print(f"Folder created: {full_path}")
