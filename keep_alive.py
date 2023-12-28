from replit import db
import os
import requests
from flask import Flask, request, make_response
from threading import Thread, Timer
from test import update_forked_repl, delete_file, delete_directory
from spin import perform
import time
import sys

app = Flask('')


def stop_repl():
  delete_directory('downloaded_files')

  os._exit(0)


  # sys.exit(0)
@app.route('/itslikelytimetoshuddown')
def down():
  print('down')
  os._exit(0)


@app.route('/')
def home():
  return "I'm alive"


@app.route(db["godsI"])
def some():
  print('on')
  response = requests.get('https://api.ipify.org')
  print(response.text)
  # Timer(10, stop_repl).start()
  return response.text


@app.route(db["transformer"], methods=['POST'])
def receive_json():
  data = request.get_json()
  password = data.get('password')
  modified = data.get('modified', [])
  added = data.get('added', [])
  removed = data.get('removed', [])
  dir_remove = data.get('dir_remove', [])

  if password == db["password"]:

    if isinstance(modified, list):
      for file in modified:
        update_forked_repl(file)

    elif isinstance(modified, str):
      update_forked_repl(modified)

    if isinstance(added, list):
      for file in added:
        update_forked_repl(file)

    elif isinstance(added, str):
      update_forked_repl(added)

    if isinstance(removed, list):
      for file in removed:
        delete_file(file)

    elif isinstance(removed, str):
      delete_file(removed)

    if isinstance(dir_remove, list):
      for file in dir_remove:
        delete_directory(file)

    elif isinstance(dir_remove, str):
      delete_directory(dir_remove)

    Timer(2, stop_repl).start()

    return 'Received', 200
  else:
    return 'Bad Request', 402


def count_down():
  Timer(160, stop_repl).start()


@app.route(db['endpoint'], methods=['POST'])
def original():
  data = request.get_json()
  password = data.get('password')
  application = data.get('application')
  method = data.get('method')
  url = data.get('url')
  if password == db["password"]:
    if application == db["appli"]:
      print("comensing perform")
      thread = Thread(target=count_down)
      thread.start()
      success = perform(url, method)
      if success:
        Timer(2, stop_repl).start()
        return 'Received', 200
      else:
        return 'Error', 400

  else:
    return 'Bad Request', 402


def run():
  # os.system("uwsgi --http :8080 --wsgi-file main.py --callable app")
  app.run(host='0.0.0.0', port=int(os.getenv('PORT', 5000)), threaded=True)


def keep_alive():
  # while True:
  t = Thread(target=run)
  # if not t.is_alive():
  t.start()
