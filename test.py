import requests
import os
from replit import db


def update_forked_repl(fileName):
  print(fileName)
  main_repl_code_url = f"{db['omegasource'] }{fileName}"

  response = requests.get(main_repl_code_url)
  print(response)
  if response.status_code == 200:
    change_code = response.text
    with open(fileName, "w") as file:

      file.write(change_code)
      print("Forked repl updated successfully.")
  else:
    print("Failed to download code from the main repl.")


def delete_file(fileName):
  # Check if the file exists
  if os.path.exists(fileName):
    # Remove the file
    os.remove(fileName)
    print(f"File '{fileName}' has been deleted.")
  else:
    print("The file does not exist.")
