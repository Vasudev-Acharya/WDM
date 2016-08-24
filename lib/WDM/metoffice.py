import urllib2
import requests,json
import pycurl
from StringIO import StringIO
import csv

class met_data():
    def __init__(self,key):
        self.key = key

    def download(self, base_url, resource, location, attribute):
        response = urllib2.urlopen("".join([base_url, resource, self.key]))

        # response = urllib2.urlopen("http://www.metoffice.gov.uk/pub/data/weather/uk/climate/datasets/Tmax/date/UK.txt?key=270ea5ad-917a-40fc-a9d9-c5f659cf1f77")
        # response = urllib2.urlopen("http://datapoint.metoffice.gov.uk/public/data/txt/wxobs/ukextremes/json/capabilities?key=270ea5ad-917a-40fc-a9d9-c5f659cf1f77")

        # url = "https://www.googleapis.com/qpxExpress/v1/trips/search?key=mykeyhere"
        # data = requests.get(url).json
        #
        # return data.read()

        buffer = StringIO()
        c = pycurl.Curl()

        c.setopt(c.URL, 'http://www.metoffice.gov.uk/pub/data/weather/uk/climate/datasets/' + attribute +'/date/'+ location +'.txt')
        c.setopt(c.WRITEDATA, buffer)
        c.perform()
        c.close()

        body = buffer.getvalue()
        return body

    def parse_tsv(self, file):
        with open(file, 'r') as f:
            result = [x.strip().split() for x in f]
            return result


# Max temp, Min temp, Mean temp, Sunshine, and Rainfall for UK, England, Wales, and Scotland regions