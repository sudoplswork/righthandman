import os, sys, subprocess
from google.genai import types

def run_python_file(working_directory, file_path, args=[]):
    try:
        input_path = file_path
        wd_abs = os.path.abspath(working_directory)
        target_abs = os.path.abspath(os.path.join(working_directory, file_path))

        # Ensure target is inside working_directory
        if os.path.commonpath([wd_abs, target_abs]) != wd_abs:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        
        # Check if the file exists
        if not os.path.isfile(target_abs):
            return f'Error: File "{file_path}" not found.'
        
        # Make sure it's a python file
        if not target_abs.endswith(".py"):
            return f'Error: "{file_path}" is not a Python file.'
        
        # unpack the args provided
        cmd = [sys.executable, target_abs, *[str(a) for a in args]]

        try:
            # pass through args, grab output from stdio, output as txt since str return, limit to working_dir
            result = subprocess.run( 
                cmd,
                capture_output=True,
                text=True,
                timeout=30,
                cwd=wd_abs,
                shell=False
            )
            #clean results
            stdout = result.stdout.strip()
            stderr = result.stderr.strip()

            if not stdout and not stderr:
                return "No output produced."

            output_parts = []
            if stdout:
                output_parts.append(f"STDOUT:\n{stdout}")
            if stderr:
                output_parts.append(f"STDERR:\n{stderr}")
            if result.returncode != 0:
                output_parts.append(f"Process exited with code {result.returncode}")

            return "\n".join(output_parts)
        except Exception as e:
            return f"Error: executing Python file: {e}"
        
        

    except Exception as e:
        return f'Error finding the python file {input_path} : {e} '
    
schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Runs a provided python file with any optional arguments provided as a list. Execution is constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The name of the python file to be executed. (must be a .py). Execution is constrained to the working directory.",
            ),
            "args":types.Schema(
                type=types.Type.ARRAY,
                description="A list of optional arguments that have been provided to the python file.",
                items=types.Schema(type=types.Type.STRING),
            ),
        },
    ),
)
