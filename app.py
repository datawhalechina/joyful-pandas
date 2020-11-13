from flask import Flask
app = Flask(__name__)

@app.route('/')
def my_index():
    return "<h1>Hello</h1>"