import os 
import shutil

def organize_files_by_extension(path):
    """
    Organize files in the specified path into folders based on their extensions.
    """
    # Validate input path
    if not os.path.isdir(path):
        print("Error: The provided path is not a directory.")
        return

    files = os.listdir(path)

    for file in files:
        if os.path.isdir(os.path.join(path, file)):
            continue  # Skip directories
        
        filename, extension = os.path.splitext(file)
        extension = extension[1:]  # Remove the dot from the extension

        # Create directory if it doesn't exist
        extension_dir = os.path.join(path, extension)
        if not os.path.exists(extension_dir):
            os.makedirs(extension_dir)

        # Move file to the corresponding directory
        try:
            shutil.move(os.path.join(path, file), os.path.join(extension_dir, file))
        except Exception as e:
            print(f"Error moving file {file}: {e}")

if __name__ == "__main__":
    path = input("Enter Path: ")
    organize_files_by_extension(path)
