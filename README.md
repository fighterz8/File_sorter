# Automated Folder Organizer
WARNING: DO NOT RUN THIS PROGRAM WHILE DOWNLOADING A FILE, ERRORS WILL OCCUR.
This project is an automated folder organizer, which monitors a specified directory and automatically sorts the files into corresponding folders based on their extensions.

## Getting Started

### Prerequisites

You need Python 3.x and the following Python packages:

- watchdog

You can install the necessary packages using pip:

```shell

pip install watchdog

Usage
To use this folder organizer, run the main.py script and pass the path of the directory you want to monitor as an argument. For example:

shell
Copy code
python main.py /path/to/your/directory
If no directory is specified, the script will monitor the current directory.

How it Works
The script uses the watchdog library to monitor the specified directory for any changes. Whenever a new file is added to the directory, the script will move it into a subdirectory named after the file's extension.

Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
