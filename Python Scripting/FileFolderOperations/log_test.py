# logging system with Python scripts helps track what’s happening during execution — 
# especially for file/folder operations
import logging
from pathlib import Path
from datetime import datetime

# --- Create a logs folder ---
log_dir = Path("logs")
log_dir.mkdir(exist_ok=True)

# --- Generate log filename based on timestamp ---
log_filename = log_dir / f"log_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"

# --- Configure logging ---
logging.basicConfig(
    level=logging.INFO,  # Set to DEBUG for more detail
    format="%(asctime)s | %(levelname)s | %(message)s",
    handlers=[
        logging.FileHandler(log_filename),
        logging.StreamHandler()  # Also print to console
    ]
)

# --- Example usage ---
logging.info("Script started.")
logging.debug("This is a debug message (you'll only see it if level=DEBUG).")
logging.warning("This is a warning.")
logging.error("An error occurred.")

try:
    # Simulate creating a folder
    test_folder = Path("output/example_folder")
    test_folder.mkdir(parents=True, exist_ok=True)
    logging.info(f"✅ Folder created at: {test_folder}")
except Exception as e:
    logging.exception("❌ Failed to create folder.")
