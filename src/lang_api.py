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
                   'Oceania',]

    lang_final = []

    if region in region_list:
        url = base_url + region
        response = requests.get(url)
        try:
            if response.status_code == 200:
                json = response.json()
                for i in range(0, len(json)):
                    lang_get = json[i]['languages']
                    lang_work = lang_get[0]['name']
                    if lang_work not in lang_final:
                        lang_final.append(lang_work)

        except KeyError:
            pass

'''
This works:
In [35]: print(lang_final)
['French', 'English', 'Samoan', 'Bislama']

In [36]: lang_work = []
    ...: for i in range(0, len(json)):
    ...:     lang_get = json[i]['languages']
    ...:     lang_work = lang_get[0]['name']
    ...:     if lang_work not in lang_final:
    ...:         lang_final.append(lang_work)

Need to put into a list and keep dupes from poplating.  But that works!ß
'''
