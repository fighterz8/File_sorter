import sys
import time
import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from File_sorter import sort_file

class FileCreatedHandler(FileSystemEventHandler):
    def on_created(self, event):
        if not event.is_directory:
            sort_file(event.src_path)

    def on_modified(self, event):
        if not event.is_directory:
            sort_file(event.src_path)

if __name__ == "__main__":
    path = sys.argv[1] if len(sys.argv) > 1 else "."

    # Sort existing files in directory
    for filename in os.listdir(path):
        file_path = os.path.join(path, filename)
        if os.path.isfile(file_path):
            sort_file(file_path)

    event_handler = FileCreatedHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()


