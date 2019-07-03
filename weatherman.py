#!/usr/bin/env python3
''' Main program. (Controller) '''

import os
import re
import datetime
import json
import requests
import dbman


class Weather:
    ''' For creating the weather class '''
    def __init__(self):
        self.city_id = 1277333                                           # City ID.
        self.today = datetime.date.today()                               # Today.
        self.day1 = datetime.date.today()
        self.day2 = self.today + datetime.timedelta(1)
        self.day3 = self.today + datetime.timedelta(2)
        self.day4 = self.today + datetime.timedelta(3)
        self.weather_data = self.get_data(self.city_id)                  # Weather data.
        self.selected_city = dbman.parse_city_id(self.city_id)           # City name.
        self.selected_time = ""
        self.selected_tmax = ""
        self.selected_tmin = ""
        self.selected_cloudiness = ""
        self.selected_windspeed = ""
        self.selected_humidity = ""
        self.print_data(self.weather_data[0])

    def get_data(self, city_id):
        ''' Collects the weather data from the api in json format. '''
        response = requests.get(f'http://api.openweathermap.org/data/2.5/forecast?id={self.city_id}&APPID=f5245c1537e27b43093b74ae91ff5d2d')
        weather_data = json.loads(response.content)['list']
        return weather_data

    def change_city(self, city_name):
        ''' Selecting a different city. '''
        temp_id = dbman.get_code(city_name)
        if temp_id:
            self.city_id = temp_id
            self.selected_city = dbman.parse_city_id(self.city_id)
            self.weather_data = self.get_data(self.city_id)

        else:
            print(f'\n"{city_name}" does not exist. PLease try again. \nEnter q to quit.\n')

    # def overview(self):
    #     ''' Printing the overview for that day. '''
    #     for dates in self.weather_data:
    #         if dates['dt_txt'].startswith(str(self.today)):
    #             print(f'\nToday\'s weather overview of {self.selected_city}.\n')
    #             dbman.print_data(dates)

    def flask_search(self, date, time):

        x_x = str(date) + " " + str(time)
        print(x_x)
        
        for dates in self.weather_data:
            if dates['dt_txt'].startswith(x_x):
                self.print_data(dates)
                break

    # def advanced_search(self, days, hours):
    #     ''' The advanced search function. '''
    #     self.today = datetime.date.today()

    #     if days == '0':
    #         pass
    #     elif days == '1':
    #         self.today = self.today + datetime.timedelta(days=1)
    #     elif days == '2':
    #         self.today = self.today + datetime.timedelta(days=2)
    #     elif days == '3':
    #         self.today = self.today + datetime.timedelta(days=3)
    #     elif days == '4':
    #         self.today = self.today + datetime.timedelta(days=4)
    #     elif days == '5':
    #         print("Logged out")
    #         os._exit(0)
    #     else:
    #         pass # Raise error in flask
        
        # # For filtering out non digit characters
        # hours_1 = re.sub(r'[^\d]', '', hours)
        # x_x = len(hours)
        # y_y = int(hours)
        # if hours_1 != hours:
        #     print('\nPlease only enter numbers. Try again')
        #     self.advanced_search()

        # # Parsing somewhat valid user input.
        # if x_x > 0 and x_x < 3 and y_y == 24 and int(days) == 4:
        #     print('Search parameter exceeds 5 days. Try again')    # You cannot go more than 4 days.
        #     self.advanced_search()
        # elif x_x > 0 and x_x < 3 and y_y == 24 and int(days) != 4:
        #     self.today = self.today + datetime.timedelta(days=1)   # Adding one more day if hours enteres is 24.
        #     print(self.today)
        # elif x_x > 0 and x_x < 3 and y_y >= 0 and y_y < 24:
        #     self.selected_hour = y_y
        # else:                                                      # Self explanatory. lol
        #     print('Our planet uses 24 hour clock.\nMr Alien, please enter an hour according to our clocks.')
        #     self.advanced_search()


        # Printing out data for valid queries.
        # self.selected_hour = hours
        # for dates in self.weather_data:
        #     x_x = self.selected_hour - int(dates['dt_txt'].split(" ")[1].split(":")[0])
        #     y_y = int(dates['dt_txt'].split(" ")[1].split(":")[0])
        #     if dates['dt_txt'].startswith(str(self.today)) and x_x == 0:
        #         print('###########################\nSelected hour is in this time window:')
        #         dbman.print_data(dates)
        #         break
        #     elif dates['dt_txt'].startswith(str(self.today)) and x_x < 3 and x_x > 0:
        #         print('###########################\nSelected hour is in this time window:')
        #         dbman.print_data(dates)
        #         break
        #     elif dates['dt_txt'].startswith(str(self.today)) and y_y >= 21 and x_x < 4:
        #         print('###########################\nSelected hour is in this time window:')
        #         dbman.print_data(dates)
            # elif dates['dt_txt'].startswith(str(self.today)) and i == len(self.weather_data):
            #     print('###########################\nSelected hour is is already passed.\nTry again.')
            #     self.advanced_search()
    
    def print_data(self, dates):
        ''' Output format for the data. '''
        self.selected_time = dates['dt_txt'][-8:-1]
        self.selected_tmax = "{0:.2f}".format(dates['main']['temp_max']-273.15) + ' Celcius'
        self.selected_tmin = "{0:.2f}".format(dates['main']['temp_min']-273.15) + ' Celcius'
        self.selected_windspeed =  str(dates['wind']['speed']) + 'mph'
        self.selected_humidity = str(dates['main']['humidity']) + '%'
        self.selected_cloudiness = dates['weather'][0]['description']
        # print('\n')


if __name__ == "__main__":
    VACATION = Weather()
