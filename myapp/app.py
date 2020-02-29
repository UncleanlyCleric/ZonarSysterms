#!/usr/bin/env python3
#pylint: disable = C0200, C0103
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

As there is a large amount of data that comes from that site, there needed to
be some curating to make sure we're only concerned with the "valid language"
data.

The way I implemented this, probably isn't the prettiest, because honestly
this is the first time I've tried to build an API using data from a second
API, but it /is/ working, so I'll call that one a win.
'''
import requests
from flask import Flask, jsonify


APP = Flask(__name__)


def lang_get(region):
    '''
    This function queries restfulcounties to grab all countries available.

    PARAM = region
    '''
    base_url = 'https://restcountries.eu/rest/v2/region/'
    lang_final = []
    url = base_url + region
    response = requests.get(url)

    try:
        if response.status_code == 200:
            json = response.json()
            for i in range(0, len(json)):
                lang_grab = json[i]['languages']
                lang_work = lang_grab[0]['name']
                if lang_work not in lang_final:
                    lang_final.append(lang_work)
            return lang_final
        return None
    except KeyError:
        return 'Invalid Key'


@APP.errorhandler(404)
def page_not_found(e):
    '''
    Giving my 404 some json love.
    '''
    return jsonify(error=404, text=str(e)), 404


@APP.route('/lang_get/api/<string:region>', methods=['GET'])
def lang_api(region):
    '''
    This is the main API call.
    '''
    region_list = ['africa', 'americas', 'asia', 'europe', 'oceania']

    if region not in region_list:
        error = {'Invalid input: valid domains are': region_list}
        return error
    final_list = {region: lang_get(region)}
    return final_list


if __name__ == '__main__':
    APP.run(debug=False, host='0.0.0.0')
