from nose.tools import *

import sys    
sys.path.append('/Users/vasudev/projects/weather_data_management/lib/')

import WDM

def setup():
    print "SETUP!"

def teardown():
    print "TEAR DOWN!"

def test_basic():
    print "I RAN!"

