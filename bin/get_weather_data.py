import django
import sys
import os
import json
import requests
from requests.auth import HTTPBasicAuth

sys.path.append("/Users/vasu/projects/WDM")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "WDM.settings")
django.setup()

import weather_data.models
from weather_data.models import Region
from weather_data.models import Weather


sys.path.append("/Users/vasu/projects/WDM/lib/WDM")
from metoffice import met_data

url = 'http://127.0.0.1:8000/region/'
loc_response_url = 'http://127.0.0.1:8000/RegionByName/'

weather_url = 'http://127.0.0.1:8000/weather/'

base_url = "http://datapoint.metoffice.gov.uk/public/data/"
resource = "val/wxfcs/all/xml/3840?res=3hourly&key="
key = "270ea5ad-917a-40fc-a9d9-c5f659cf1f77"
down_data = met_data(key)


Locations=['UK','England','Wales','Scotland']
Attr=['Tmax','Tmin','Tmean','Sunshine','Rainfall']

for loc in Locations:
    payload = {'name': loc}
    r = requests.post(url, data=payload, auth=HTTPBasicAuth('vasu', os.environ['DB_PWD']))

    print r.text

    payload = {'loc_name': loc}
    loc_response = requests.get(loc_response_url+loc+'/', auth=HTTPBasicAuth('vasu', os.environ['DB_PWD']))

    print loc_response.json

    reg = Region.objects.get(name=loc)

    for att in Attr:
        print loc + " :: " + att
        result = down_data.download(base_url, resource, loc, att)

        f = open(loc + "_" + att + ".tsv", 'w')
        f.write(str(result))
        f.close()

        result = down_data.parse_tsv(loc + "_" + att + ".tsv")

        for i in range(len(result)):
            for j in range(len(result[i])):
                if result[i][0].isdigit():
                    # payload = {'region': reg, 'type':att,'month':result[7][j],'year':result[i][0],'value':result[i][j]}
                    # weather_post = requests.post(weather_url, data=payload, auth=HTTPBasicAuth('vasu', os.environ['DB_PWD']))
                    #
                    # print weather_post.text
                    #
                    # # payload = {'loc_name': loc}
                    # # loc_response = requests.get(loc_response_url + loc + '/', auth=HTTPBasicAuth('vasu', os.environ['DB_PWD']))

                    weather = Weather.objects.filter(region=reg.id,type=att,year=result[i][0],month=result[7][j])

                    if weather.exists():
                        print "Weather info for " + loc + "\'s " + att + " for Year/Month : " + result[i][0] + "/" + result[7][j] + " is already registered as : " + result[i][j]
                    else:
                        weather = Weather(region=reg,type=att,year=result[i][0],month=result[7][j],value=result[i][j])
                        weather.save()
                        print "Stored Weather info for " + loc + "\'s " + att + " for Year/Month : " + result[i][0] + "/" + result[7][j] + " as : " + result[i][j]