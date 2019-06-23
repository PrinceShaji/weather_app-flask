#!/usr/bin/env python3

''' Main app for the flask weather app. '''

import requests
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def homepahe():
    return render_template('index.html')








if __name__ == "__main__":
    app.run(debug=True)