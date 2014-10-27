"""
Test the functions in the `common` module
"""

import pytest
import sys
sys.path.append('src')

from common import (datetime_tuple, get_utc_time, get_local_time, shell_split,
                    find_argument_quoted, find_argument_unquoted,
                    parse_str_to_secs, parse_secs_to_str)
import time
from datetime import timedelta
import datetime

def test_datetime_tuple():
    time.timezone = 0
    time.altzone = 0

    assert datetime_tuple('20130226T06:23:12') == datetime.datetime(2013, 2, 26, 6, 23, 12)
    assert datetime_tuple('2013-02-26T06:23:12+02:00') == datetime.datetime(2013, 2, 26, 4, 23, 12)

    time.timezone = -3600
    time.altzone = -3600

    assert datetime_tuple('20130226T07:23:12') == datetime.datetime(2013, 2, 26, 8, 23, 12)
    assert datetime_tuple('2013-02-26T07:23:12+02:00') == datetime.datetime(2013, 2, 26, 6, 23, 12)

def test_utc_time():
    delta = timedelta(seconds=-3600)
    d = datetime.datetime.now()
    time.timezone = -3600; time.altzone = -3600
    assert get_utc_time(local_time=d) == d + delta

def test_local_time():
    delta = timedelta(seconds=-3600)
    d = datetime.datetime.now()
    time.timezone = -3600
    time.altzone = -3600
    assert get_local_time(d) == d - delta

#def find_delayed_tag(message):

def test_shell_split():
    assert shell_split('"sdf 1" "toto 2"') == ['sdf 1', 'toto 2']
    assert shell_split('toto "titi"') == ['toto', 'titi']
    assert shell_split('toto ""') == ['toto', '']
    assert shell_split('to"to titi "a" b') == ['to"to', 'titi', 'a', 'b']
    assert shell_split('"toto titi" toto ""') == ['toto titi', 'toto', '']
    assert shell_split('toto "titi') == ['toto', 'titi']

def test_argument_quoted():
    assert find_argument_quoted(4, 'toto titi tata') == 3
    assert find_argument_quoted(4, '"toto titi" tata') == 0
    assert find_argument_quoted(8, '"toto" "titi tata"') == 1
    assert find_argument_quoted(8, '"toto" "titi tata') == 1
    assert find_argument_quoted(3, '"toto" "titi tata') == 0
    assert find_argument_quoted(18, '"toto" "titi tata" ') == 2

def test_argument_unquoted():
    assert find_argument_unquoted(2, 'toto titi tata') == 0
    assert find_argument_unquoted(3, 'toto titi tata') == 0
    assert find_argument_unquoted(6, 'toto titi tata') == 1
    assert find_argument_unquoted(4, 'toto titi tata') == 3
    assert find_argument_unquoted(25, 'toto titi tata') == 3

def test_parse_str_to_secs():
    assert parse_str_to_secs("1d3m1h") == 90180
    assert parse_str_to_secs("1d3mfaiiiiil") == 0

def test_parse_secs_to_str():
    assert  parse_secs_to_str(3601) == '1h1s'
