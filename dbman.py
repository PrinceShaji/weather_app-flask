#!/usr/bin/env python3
''' Manages the database part '''

import json
import re

# Loading the json file (complete list of cities)
FIN = open('databases/city.list.json', 'r')
DB = json.load(FIN)
FIN.close()

def get_code(search):
    ''' For getting city id. '''
    search = "".join(re.sub(r' +', ' ', search))
    search = search.strip().title()
    for places in DB:
        if places['name'] == search:
            return places['id']

def parse_city_id(city_id):
    ''' Getting city name from the db. '''
    for cities in DB:
        if cities['id'] == city_id:
            return cities['name']




if __name__ == "__main__":
    RESPONSE = get_code(input("Enter city name: "))
    if RESPONSE:
        print("\nCity code is:", RESPONSE)
    else:
        print("Not a valid city name. Try again.")
