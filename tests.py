from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content

# Tests for getting file info:
# print(f'Test One: get_files_info("calculator", ".") {get_files_info("calculator", ".")}')
# print(f'Test Two: get_files_info("calculator", "pkg") {get_files_info("calculator", "pkg")}')
# print(f'Test Three: get_files_info("calculator", "/bin") {get_files_info("calculator", "/bin")}') 
# print(f'Test Four: get_files_info("calculator", "../") {get_files_info("calculator", "../")}') 

# Tests for getting file content:

# print(f'Result for get_file_content("calculator", "lorem.txt"): {get_file_content("calculator", "lorem.txt")}' )
print(f'Result for get_file_content("calculator", "main.py"): {get_file_content("calculator", "main.py")}' )
print(f'Result for get_file_content("calculator", "pkg/calculator.py"): {get_file_content("calculator", "pkg/calculator.py")}' )
print(f'Result for get_file_content("calculator", "/bin/cat"): { get_file_content("calculator", "/bin/cat")}' )
print(f'Result for get_file_content("calculator", "pkg/does_not_exist.py"): { get_file_content("calculator", "pkg/does_not_exist.py")}' ) # #error str expected
