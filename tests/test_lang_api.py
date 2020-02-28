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
