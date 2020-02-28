#!/usr/bin/env python3
'''
Testing the language API lang_api.py
'''
import pytest
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
