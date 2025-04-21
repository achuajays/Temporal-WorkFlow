import os
import shutil
from temporalio import activity


@activity.defn
def move_files(source_folder: str, destination_folder: str) -> str:
    import os
    import shutil

    # Ensure destination folder exists
    os.makedirs(destination_folder, exist_ok=True)

    # Get list of files in source folder
    files = os.listdir(source_folder)
    moved_count = 0

    # Move each file to destination folder
    for file in files:
        source_path = os.path.join(source_folder, file)
        destination_path = os.path.join(destination_folder, file)

        if os.path.isfile(source_path):
            shutil.copy2(source_path, destination_path)

            # Check before deleting to avoid FileNotFoundError
            if os.path.exists(source_path):
                os.remove(source_path)

            moved_count += 1

    return f"Moved {moved_count} files from {source_folder} to {destination_folder}"