import os


def rename_images_in_directory(directory):
    # Get the name of the directory
    dir_name = os.path.basename(os.path.normpath(directory))

    # List all .jpg files in the directory
    jpg_files = [f for f in os.listdir(directory) if f.endswith('.jpg')]

    # Sort the files to maintain a consistent order
    jpg_files.sort()

    # Loop through and rename each file
    for index, file_name in enumerate(jpg_files, start=1):
        # Create the new name in the format "Dir_Name_1.jpg", "Dir_Name_2.jpg", etc.
        new_name = f"{dir_name}_{index}.jpg"

        # Get the full path of the current and new file names
        old_file_path = os.path.join(directory, file_name)
        new_file_path = os.path.join(directory, new_name)

        # Rename the file
        os.rename(old_file_path, new_file_path)
        print(f"Renamed '{file_name}' to '{new_name}'")




