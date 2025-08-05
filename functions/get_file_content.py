import os

MAX_CHARS = 10000

def get_file_content(working_directory, file_path):
    if not isInsideDirectory(working_directory=working_directory, filepath=file_path):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    fullpath = os.path.abspath(os.path.join(working_directory, file_path))
    if not os.path.isfile(fullpath):
        return f'Error: File not found or is not a regular file: "{file_path}"'
    try:
        with open(fullpath, "r") as f:
            file_content_string = f.read(MAX_CHARS)
            file_remainder = f.read(1)
            if not file_remainder == "":
                file_content_string += f'[...File "{file_path}" truncated at 10000 characters]'
            return file_content_string
    except Exception as e:
        return f"Error: {e}"

def isInsideDirectory(working_directory, filepath):
  return os.path.abspath(os.path.join(working_directory, filepath)).startswith(os.path.abspath(working_directory))