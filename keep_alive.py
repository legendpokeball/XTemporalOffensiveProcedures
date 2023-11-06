from replit import db
import os
import requests
from flask import Flask, request
from threading import Thread
from test import update_forked_repl, delete_file
from spin import perform

app = Flask('')


@app.route('/')
def home():
  return "I'm alive"


@app.route(db["godsI"])
def some():
  print('on')
  response = requests.get('https://api.ipify.org')
  print(response.text)
  return response.text


@app.route(db["transformer"], methods=['POST'])
def receive_json():
  data = request.get_json()
  password = data.get('password')
  modified = data.get('modified', [])
  added = data.get('added', [])
  removed = data.get('removed', [])

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

    return 'Received', 200
  else:
    return 'Bad Request', 402


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
      success = perform(url, method)
      if success:
        return 'Received', 200
      else:
        return 'Error', 400

    return 'Received', 200
  else:
    return 'Bad Request', 402


def run():
  app.run(host='0.0.0.0', port=int(os.getenv('PORT', 8080)))


def keep_alive():
  t = Thread(target=run)
  t.start()