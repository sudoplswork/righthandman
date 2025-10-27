import os
from google.genai import types

def get_files_info(working_directory, directory="."):
    try:
        # Build absolute paths
        full_path = os.path.abspath(os.path.join(working_directory, directory))
        working_directory_abs = os.path.abspath(working_directory)

        # Ensure full_path is inside the working_directory
        if not full_path.startswith(working_directory_abs):
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

        # Check if the target is a valid directory
        if not os.path.isdir(full_path):
            return f'Error: "{directory}" is not a directory'
        
        # Build directory contents info
        entries = []
        for name in os.listdir(full_path):
            path = os.path.join(full_path, name)
            size = os.path.getsize(path)
            is_dir = os.path.isdir(path)
            entries.append(f"- {name}: file_size={size} bytes, is_dir={is_dir}")

        return "\n".join(entries)
        
    except Exception as e:
        return f"Error listing files: {str(e)}"
    

schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)
    

