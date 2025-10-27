import os
from google.genai import types
from functions.get_file_content import get_file_content
from functions.get_files_info import get_files_info
from functions.run_python_file import run_python_file
from functions.write_file import write_file



# Helper function to make this cleaner for output below
def make_tool_response(name, result):
    return types.Content(
        role="tool",
        parts=[
            types.Part.from_function_response(
                name=name,
                response={"result": result},
            )
        ],
    )



def call_function(function_call_part, verbose=False):

    # Google cant get a grip on what they return to this API...
    if isinstance(function_call_part, dict):
        fnc_name = function_call_part.get("name")
        raw_args = function_call_part.get("args", {}) or {}
    else:
        fnc_name = getattr(function_call_part, "name", None)
        raw_args = getattr(function_call_part, "args", {}) or {}
    
    if not fnc_name:
        return types.Content(
            role="tool",
            parts=[types.Part.from_function_response(
                name="__invalid__",
                response={"error": "Missing function name in function_call_part"},
            )],
        )



    # if verbose print the args too
    if verbose:
        print(f"Calling function: {function_call_part.name}({function_call_part.args})")
    print(f" - Calling function: {function_call_part.name}")

    # hardcoding working_directory string 
    fnc_name = function_call_part.name
    fnc_args = dict(function_call_part.args)
    fnc_args["working_directory"] = os.path.abspath("./calculator")


    # match to call str
    match fnc_name:
        case "get_file_content":
            return make_tool_response(fnc_name, get_file_content(**fnc_args))
        case "get_files_info":
            return make_tool_response(fnc_name, get_files_info(**fnc_args))
        case "write_file":
            return make_tool_response(fnc_name, write_file(**fnc_args))
        case "run_python_file":
            return make_tool_response(fnc_name, run_python_file(**fnc_args))
        case _:
            return types.Content(
                role="tool",
                parts=[
                    types.Part.from_function_response(
                        name=fnc_name,
                        response={"error": f"Unknown function: {fnc_name}"},
                    )
                ],
            )
