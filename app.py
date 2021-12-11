import os
from flask import Flask, render_template, redirect, jsonify, request
from db import get, create

DEBUG = True
PORT = int(os.environ.get('PORT', 5000))
HOST = '127.0.0.1'

app = Flask(__name__)
app.secret_key = 'asdnafnj#46sjsnvd(*$43sfjkndkjvnskb6441531@#$$6sddf'

# def implicit():
#     from google.cloud import storage

#     # If you don't specify credentials when constructing the client, the
#     # client library will look for credentials in the environment.
#     storage_client = storage.Client()

#     # Make an authenticated API request
#     buckets = list(storage_client.list_buckets())
#     print(buckets)

@app.route('/hello')
def hello():
    return 'Hello, World!'
    
@app.route('/')
def header():
    print(DEBUG)
    return render_template('index.html', isLogedIn = False)


@app.route('/auth')
def login():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/connectdb')
def check():
    data = get()
    print(data)
    return data  

if __name__ == '__main__':
	app.run(debug=DEBUG,host = HOST, port = PORT)
