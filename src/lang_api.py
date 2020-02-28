#!/usr/bin/env python3
'''
This is a valid language list per region API.  The goal is to implement an
API that consumes a region from a specific list, and return a list of valid
languages that exist there.

The data is being parsed from the API at https://restcountries.eu.

The regions to be used are:
Africa
Americas
Asia
Europe
Oceania

 '''
import requests
from flask import Flask
from flask_restful import Resource, Api


app = Flask(__name__)
api = Api(app)


def lang_get(region):
    '''
    This function queries restfulcounties to grab all countries available.
    Languages will be parsed out in another function.

    PARAM = region
    '''
    base_url = 'https://restcountries.eu/rest/v2/region/'
    region_list = ['Africa',
                   'Americas',
                   'Asia',
                   'Europe',
                   'Oceania']


    if region in region_list:
        url = base_url + region
        response = requests.get(url)
        try:
            if response.status_code == 200:
                json = response.json()
                for data in json['language']:
                    print()

        except KeyError:
            pass
