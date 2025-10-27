import os
from google.genai import types
from config import MAX_CHARS

def get_file_content(working_directory, file_path):
    try:
        # Keep the original for messages
        input_path = file_path

        # Absolute, containment-safe paths
        wd_abs = os.path.abspath(working_directory)
        target_abs = os.path.abspath(os.path.join(working_directory, file_path))

        # Ensure target is inside working_directory
        if os.path.commonpath([wd_abs, target_abs]) != wd_abs:
            return f'Error: Cannot read "{input_path}" as it is outside the permitted working directory'

        # Must be a regular file
        if not os.path.isfile(target_abs):
            return f'Error: File not found or is not a regular file: "{input_path}"'

        # Read as text; replace undecodable bytes to avoid crashes
        with open(target_abs, "r", encoding="utf-8", errors="replace") as f:
            content = f.read()

        # Truncate if needed and append the required note
        if len(content) > MAX_CHARS:
            return content[:MAX_CHARS] + f'\n[...File "{input_path}" truncated at {MAX_CHARS} characters]'

        return content

    except Exception as e:
        return f"Error reading the file {file_path}: {e}"
    

schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Reads the content of the provided file name. Execution is constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The name of the file to be read. Execution is constrained to the working directory.",
            ),
        },
    ),
)
