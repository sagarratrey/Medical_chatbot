import os
from pathlib import Path
import logging

logging.basicConfig(level = logging.INFO, format= '[%(asctime)s : %(message)s: ]')

file_folder_structure = [
    "src/__init__.py",
    "src/helper.py",
    "src/prompt.py",
    "setup.py",
    ".env",
    "app.py",
    "research/try.ipynb"

]


for filepath in file_folder_structure:

    filepath = Path(filepath)      #automatically take care slash
    filedir, filename = os.path.split(filepath)

    if (filedir != ""):
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"creating file directory {filedir} having filename {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0): 
        # second check is when it already exists and having some storage inside it
        with open (filepath, "w") as f:
            pass
        logging.info(f"creating empty file {filename}")
    else:
        logging.info(f"filename {filename} already exists")