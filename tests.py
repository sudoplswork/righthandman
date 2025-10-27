# project_root/tests.py

from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.write_file import write_file
from functions.run_python_file import run_python_file

# ───────── Kept from before (commented exactly as-is) ─────────
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

# ───────── Tests for running Python files (new section) ─────────

print(f'Result for run_python_file("calculator", "main.py"): {run_python_file("calculator", "main.py")}')
print(f'Result for run_python_file("calculator", "main.py", ["3 + 5"]): {run_python_file("calculator", "main.py", ["3 + 5"])}')
print(f'Result for run_python_file("calculator", "tests.py"): {run_python_file("calculator", "tests.py")}')
print(f'Result for run_python_file("calculator", "../main.py"): {run_python_file("calculator", "../main.py")}')
print(f'Result for run_python_file("calculator", "nonexistent.py"): {run_python_file("calculator", "nonexistent.py")}')
print(f'Result for run_python_file("calculator", "lorem.txt"): {run_python_file("calculator", "lorem.txt")}')
