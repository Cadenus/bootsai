import os
import subprocess
from .get_files_info import isInsideDirectory

def run_python_file(working_directory, file_path, args=[]):
    if not isInsideDirectory(working_directory=working_directory, filepath=file_path):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

    fullpath = os.path.abspath(os.path.join(working_directory, file_path))

    if not os.path.isfile(fullpath):
      return f'Error: File "{file_path}" not found.'
    
    if not file_path.endswith('.py'):
       return f'Error: "{file_path}" is not a Python file.'
    
    try:
      timeout = 30
      command = ["python3", fullpath]
      command.extend(args)
      proc = subprocess.run(command, timeout=timeout, capture_output=True)
      stdout = f'STDOUT: {proc.stdout.decode('utf-8')}'
      stderr = f'STDERR: {proc.stderr.decode('utf-8')}'
      exitCode = proc.returncode
      result = ""
      if stdout == "" and stderr == "":
         return "No output produced."
      result = f'{stdout}\n{stderr}'
      if exitCode != 0: 
         result = f'{result}\nProcess exited with code {exitCode}'
      return result
    except Exception as e: 
       return f"Error: executing Python file: {e}"