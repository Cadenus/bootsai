import os

def write_file(working_directory, file_path, content):
    if not isInsideDirectory(working_directory, file_path):
       return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    fullpath = os.path.abspath(os.path.join(working_directory, file_path))
    try:
        write_mode = "x"
        if os.path.exists(fullpath):
            write_mode = "w"
        with open(fullpath, write_mode) as f:
            f.write(content)
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:
       return f"Error: {e}"    
    

def isInsideDirectory(working_directory, filepath):
  return os.path.abspath(os.path.join(working_directory, filepath)).startswith(os.path.abspath(working_directory))