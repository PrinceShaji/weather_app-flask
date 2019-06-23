#!/usr/bin/env python3

''' Main app for the flask weather app. '''

import requests
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def homepage():
    if request.method == "POST":
        return render_template('error.html')
        #Get city method
        #If true, get the data for city
        #return the new page
    else:
        return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)