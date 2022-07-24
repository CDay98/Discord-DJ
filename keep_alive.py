from flask import Flask
from threading import Thread
import threading

app = Flask('')

@app.route('/')
def home():
  myString = ''
  with open('Logs/website.txt') as g:
    startup_lines = g.readlines()
    for i in startup_lines:
      myString += f"{i}"
  myString += "<p style='color:#149414'>"
  with open('Logs/requests.txt') as f:
    lines = f.readlines()
    for line in lines:
      myString += f"- {line} <br>"
    return myString

threading.Timer(10, home).start()
home()
      
def run():
  app.run(
		host='0.0.0.0',
		port=8080
	)

def keep_alive():
	'''
	Creates and starts new thread that runs the function run.
	'''
	t = Thread(target=run)
	t.start()