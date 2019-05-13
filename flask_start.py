from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/wibble')
def wibble():
    return 'This is my pointless new page.'