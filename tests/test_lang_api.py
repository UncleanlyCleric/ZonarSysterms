#!/usr/bin/env python3
'''
Testing the language API lang_api.py
'''
import pytest
import requests
import lang_api as l

def test_lang_get():
    '''
    Testing the call and parsing from https://restcountries.eu
    '''
    region = 'oceania'
    result = l.lang_get(region)

    assert result == ['English', 'French', 'Samoan', 'Bislama']


def test_lang_get_error():
    '''
    Lets test a keyerror
    '''
    region = 'brazil'
    result = l.lang_get(region)
    assert result == None


def test_index_page():
    '''
    Is the page working?
    '''
    url = 'http://127.0.0.1:5000/lang_get/api/africa'
    r = requests.get(url)
    assert r.status_code == 200


def test_index_page_invalid():
    '''
    Lets try an invalid string
    '''
    url = 'http://127.0.0.1:5000/lang_get/api/none'
    r = requests.get(url)
    assert r.status_code == 200


def test_404_page():
    '''
    json 404
    '''
    url = 'http://127.0.0.1:5000/lang_get/api/'
    r = requests.get(url)
    assert r.status_code == 404
    assert '{"error":404,"text":"404 Not Found: The requested URL was not found on the server. If you entered the URL manually please check your spelling and try again."}' 
