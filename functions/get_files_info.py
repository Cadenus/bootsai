import os
 
def get_files_info(working_directory, directory=None):
  try:
    fullpath = os.path.join(working_directory, directory)
    if not isInsideDirectory(working_directory=working_directory, filepath=directory):
      print(f'Error: Cannot list "{directory}" as it is outside the permitted working directory')
      return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    if not os.path.isdir(fullpath):
      print(f'Error: "{directory}" is not a directory')
      return f'Error: "{directory}" is not a directory'
    
    fullAbsPath = os.path.abspath(fullpath)
    print(f"FullAbsPath: [{fullAbsPath}]")
    listDirectory = os.listdir(fullAbsPath)
    print(f"len({len(listDirectory)}): [{len(listDirectory)}]")
    result = ""
    for item in listDirectory:
      fullItemAbsPath = os.path.abspath(os.path.join(fullAbsPath, item))
      print(f"- {item}: file_size={os.path.getsize(fullItemAbsPath)} bytes, is_dir={os.path.isdir(fullItemAbsPath)}")
      result += f"- {item}: file_size={os.path.getsize(fullItemAbsPath)} bytes, is_dir={os.path.isdir(fullItemAbsPath)}\n"
    return result
  except Exception as e:
    return f"Error:{e}"

def isInsideDirectory(working_directory, filepath):
  return os.path.abspath(os.path.join(working_directory, filepath)).startswith(os.path.abspath(working_directory))