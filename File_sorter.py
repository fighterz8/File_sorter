import os
import shutil
from utils import create_directory_if_not_exists

def sort_file(file_path):
    file_name = os.path.basename(file_path)
    file_extension = os.path.splitext(file_name)[1][1:]  # Get file extension without the dot

    # Skip sorting if the file is one of the script files
    if file_name in ["main.py", "File_sorter.py", "utils.py"]:
        return

    directory = os.path.join(os.path.dirname(file_path), file_extension)

    create_directory_if_not_exists(directory)

    destination = os.path.join(directory, file_name)

    shutil.move(file_path, destination)
