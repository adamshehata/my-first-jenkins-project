from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, My First Jenkins Project!'
    #This is a test please work pookie wookie
