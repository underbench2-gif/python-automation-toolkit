import os
import shutil

def organize_folder(path):
    """
    Organizes files in a folder by their extension.
    """
    if not os.path.exists(path):
        print(f"Path {path} does not exist.")
        return

    for filename in os.listdir(path):
        if os.path.isfile(os.path.join(path, filename)):
            ext = filename.split('.')[-1].lower() if '.' in filename else 'no_extension'
            
            dest_folder = os.path.join(path, ext)
            if not os.path.exists(dest_folder):
                os.makedirs(dest_folder)
            
            shutil.move(os.path.join(path, filename), os.path.join(dest_folder, filename))
            print(f"Moved {filename} to {dest_folder}")

if __name__ == "__main__":
    # Example usage: organize the current directory
    # organize_folder('.')
    print("File Organizer script ready. Uncomment the call in __main__ to use.")
