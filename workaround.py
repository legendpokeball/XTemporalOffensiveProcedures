import fileinput
import subprocess


def update_executable_path():
  # Run the shell command and capture the output
  output = subprocess.check_output(["which",
                                    "chromedriver"]).decode("utf-8").strip()

  return output
