import os
from get_files_info import isInsideDirectory

def run_python_file(working_directory, file_path, args=[]):
    if not isInsideDirectory(working_directory=working_directory, filepath=file_path):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

    fullpath = os.path.abspath(os.path.join(working_directory, file_path))

    if not os.path.isfile(fullpath):
        return f'Error: File not found or is not a regular file: "{file_path}"'