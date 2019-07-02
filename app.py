#!/usr/bin/env python3

''' Main app for the flask weather app. '''

import requests
from flask import Flask, render_template, request, redirect, url_for
import dbman
from weatherman import Weather
from flask_wtf import FlaskForm
from wtforms import SelectField, Form, StringField, SubmitField
from flask_table import Table, Col
from datetime import timedelta
app = Flask(__name__)
app.config['SECRET_KEY'] = '3d6f45a5fc12445dbac2f59c3b6c7cb1'


a = {
    'city': 'bangalore',
    'time': '25 jan',
    'temp_max': '23',
    'temp_min': '21',
    'cloudiness': 'Partly Cloudy',
    'select_date': '',
    'select_time': ''
}

vacation = Weather()

@app.route('/', methods = ['GET', 'POST'])
def homepage():
    if request.method == "POST":
        city = request.form.get('city_name')
        date = request.form.get('select_date')
        time = request.form.get('select_time')
        vacation.change_city(city)
        vacation.flask_search(date, time)
        print(vacation.selected_city)
        return render_template('index.html', a=a, vacation=vacation)
    else:
        return render_template('index.html', a=a, vacation=vacation)

@app.route('/advanced', methods = ['GET', 'POST'])
def advanced():
    return redirect(url_for('homepage'))


if __name__ == "__main__":
    app.run(debug=True)
    