import os

def get_files_info(working_directory, directory=None):
  listdr = os.listdir(working_directory)
  print(listdr)
  if directory not in listdr:
    print(f'Error: Cannot list "{directory}" as it is outside the permitted working directory')
  elif directory != None:
    try:
      os.path.join(working_directory,directory)
      listDirectory = os.listdir(f"{working_directory}/{directory}")
      print(listDirectory)
      for item in listDirectory:
        print(f"{item.}")
    except NotADirectoryError as e:
      print(f'Error: "{directory}" is not a directory')


def main():
  get_files_info("/Users/a616024/bootdev/bootsai", "main.py")

main()