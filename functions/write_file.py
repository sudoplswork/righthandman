import os

def write_file(working_directory, file_path, content):
    try:
        # Keep the original for messages
        input_path = file_path

        # Absolute, containment-safe paths
        wd_abs = os.path.abspath(working_directory)
        target_abs = os.path.abspath(os.path.join(working_directory, file_path))

        # Ensure target is inside working_directory
        if os.path.commonpath([wd_abs, target_abs]) != wd_abs:
            return f'Error: Cannot write "{input_path}" as it is outside the permitted working directory'

        # Check if file path actually exists, add folders if needed and don't shit if they exist already
        dir_name = os.path.dirname(target_abs)
        if dir_name:
            os.makedirs(dir_name, exist_ok=True)

        # Open and write the target file
        with open(target_abs, "w", encoding="utf-8", errors="replace") as f:
            f.write(content)
            return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'

        

    except Exception as e:
        return f"Error while writing {file_path}: {e}"