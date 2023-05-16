from flask import Flask
from threading import Thread
from flask import render_template##

app = Flask('')

@app.route('/')
def home():
    #return "Life is Pain xd"
    return render_template('kurwa2.html')##

def run():
  app.run(host='0.0.0.0',port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()


@app.route('/functionality')
def func():
    return render_template('functionality.html')