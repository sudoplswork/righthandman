# project_root/tests.py

from functions.get_files_info import get_files_info, schema_get_files_info
from functions.get_file_content import get_file_content, schema_get_file_content
from functions.write_file import write_file, schema_write_file
from functions.run_python_file import run_python_file, schema_run_python_file
from google.genai import types

# 
# Tests for getting file info:
# print(f'Test One: get_files_info("calculator", ".") {get_files_info("calculator", ".")}')
# print(f'Test Two: get_files_info("calculator", "pkg") {get_files_info("calculator", "pkg")}')
# print(f'Test Three: get_files_info("calculator", "/bin") {get_files_info("calculator", "/bin")}') 
# print(f'Test Four: get_files_info("calculator", "../") {get_files_info("calculator", "../")}') 

# Tests for getting file content:
# print(f'Result for get_file_content("calculator", "lorem.txt"): {get_file_content("calculator", "lorem.txt")}' )
# print(f'Result for get_file_content("calculator", "main.py"): {get_file_content("calculator", "main.py")}' )
# print(f'Result for get_file_content("calculator", "pkg/calculator.py"): {get_file_content("calculator", "pkg/calculator.py")}' )
# print(f'Result for get_file_content("calculator", "/bin/cat"): { get_file_content("calculator", "/bin/cat")}' )
# print(f'Result for get_file_content("calculator", "pkg/does_not_exist.py"): { get_file_content("calculator", "pkg/does_not_exist.py")}' )

# Tests for writing files:
# print(f'Result for write 1 {write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")}')
# print(f'Result for write 2 {write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")}')
# print(f'Result for write 3 {write_file("calculator", "/tmp/temp.txt", "this should not be allowed")}')

# Tests for running files:
# print(f'Result for run_python_file("calculator", "main.py"): {run_python_file("calculator", "main.py")}')
# print(f'Result for run_python_file("calculator", "main.py", ["3 + 5"]): {run_python_file("calculator", "main.py", ["3 + 5"])}')
# print(f'Result for run_python_file("calculator", "tests.py"): {run_python_file("calculator", "tests.py")}')
# print(f'Result for run_python_file("calculator", "../main.py"): {run_python_file("calculator", "../main.py")}')
# print(f'Result for run_python_file("calculator", "nonexistent.py"): {run_python_file("calculator", "nonexistent.py")}')
# print(f'Result for run_python_file("calculator", "lorem.txt"): {run_python_file("calculator", "lorem.txt")}')


# ───────── Schema sanity prints ─────────
print("── Schema sanity checks ──")

# get_files_info
gf_props = (schema_get_files_info.parameters.properties or {})
print(f"get_files_info.name: {schema_get_files_info.name}")
print(f"get_files_info has 'directory': {'directory' in gf_props}")
if 'directory' in gf_props:
    print(f"  'directory' type is STRING: {gf_props['directory'].type == types.Type.STRING}")

# get_file_content
gfc_props = (schema_get_file_content.parameters.properties or {})
print(f"\nget_file_content.name: {schema_get_file_content.name}")
print(f"get_file_content has 'file_path': {'file_path' in gfc_props}")
if 'file_path' in gfc_props:
    print(f"  'file_path' type is STRING: {gfc_props['file_path'].type == types.Type.STRING}")

# write_file
wf_props = (schema_write_file.parameters.properties or {})
print(f"\nwrite_file.name: {schema_write_file.name}")
print(f"write_file has 'file_path': {'file_path' in wf_props}")
print(f"write_file has 'content': {'content' in wf_props}")
if 'file_path' in wf_props:
    print(f"  'file_path' type is STRING: {wf_props['file_path'].type == types.Type.STRING}")
if 'content' in wf_props:
    print(f"  'content' type is STRING: {wf_props['content'].type == types.Type.STRING}")

# run_python_file
rpf_props = (schema_run_python_file.parameters.properties or {})
print(f"\nrun_python_file.name: {schema_run_python_file.name}")
print(f"run_python_file has 'file_path': {'file_path' in rpf_props}")
print(f"run_python_file has 'args': {'args' in rpf_props}")
if 'file_path' in rpf_props:
    print(f"  'file_path' type is STRING: {rpf_props['file_path'].type == types.Type.STRING}")
if 'args' in rpf_props:
    args_schema = rpf_props['args']
    print(f"  'args' type is ARRAY: {args_schema.type == types.Type.ARRAY}")
    items_type = getattr(getattr(args_schema, 'items', None), 'type', None)
    print(f"  'args.items' type is STRING: {items_type == types.Type.STRING}")

# ───────── Assignment-style prompt → function runs ─────────
print("\n── Prompt → function results ──")

# "read the contents of main.py" -> get_file_content({'file_path': 'main.py'})
print("Prompt: read the contents of main.py")
print(get_file_content("calculator", "main.py"))

# "write 'hello' to main.txt" -> write_file({'file_path': 'main.txt', 'content': 'hello'})
print("\nPrompt: write 'hello' to main.txt")
print(write_file("calculator", "main.txt", "hello"))

# "run main.py" -> run_python_file({'file_path': 'main.py'})
print("\nPrompt: run main.py")
print(run_python_file("calculator", "main.py"))

# "list the contents of the pkg directory" -> get_files_info({'directory': 'pkg'})
print("\nPrompt: list the contents of the pkg directory")
print(get_files_info("calculator", "pkg"))
