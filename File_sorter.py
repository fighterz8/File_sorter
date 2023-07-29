import os
import shutil
from utils import create_directory_if_not_exists

def sort_file(file_path):
    if not os.path.exists(file_path):
        return

    file_name = os.path.basename(file_path)
    file_extension = os.path.splitext(file_name)[1][1:]  # Get file extension without the dot

    # Skip sorting if the file is one of the script files or a temporary file
    if file_name in ["main.py", "File_sorter.py", "utils.py"] or file_extension == "tmp":
        return

    directory = os.path.join(os.path.dirname(file_path), file_extension)

    create_directory_if_not_exists(directory)

    destination = os.path.join(directory, file_name)

    if os.path.exists(file_path):
        shutil.move(file_path, destination)

