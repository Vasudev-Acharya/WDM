import django
import sys
import os

sys.path.append("/Users/vasu/projects/WDM")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "WDM.settings")
django.setup()

import weather_data.models
from weather_data.models import Region
from weather_data.models import Weather


sys.path.append("/Users/vasu/projects/WDM/lib/WDM")
from metoffice import met_data

base_url = "http://datapoint.metoffice.gov.uk/public/data/"
resource = "val/wxfcs/all/xml/3840?res=3hourly&key="
key = "270ea5ad-917a-40fc-a9d9-c5f659cf1f77"

Locations=['UK','England','Wales','Scotland']
Attr=['Tmax','Tmin','Tmean','Sunshine','Rainfall']

data = met_data(key)

for loc in Locations:

    try:
        reg = Region.objects.get(name=loc)
        print "Location \'" + loc + "\' ALready present in Database."
    except:
        reg = Region(name=loc)
        reg.save()

    reg = Region.objects.get(name=loc)

    for att in Attr:
        print loc + " :: " + att
        result = data.download(base_url, resource, loc, att)

        f = open(loc + "_" + att + ".tsv", 'w')
        f.write(str(result))
        f.close()

        result = data.parse_tsv(loc + "_" + att + ".tsv")

        for i in range(len(result)):
            for j in range(len(result[i])):
                if result[i][0].isdigit():

                    weather = Weather.objects.filter(region=reg.id,type=att,year=result[i][0],month=result[7][j])

                    if weather.exists():
                        print "Weather info for " + loc + "\'s " + att + " for Year/Month : " + result[i][0] + "/" + result[7][j] + " is already registered as : " + result[i][j]
                    else:
                        weather = Weather(region=reg,type=att,year=result[i][0],month=result[7][j],value=result[i][j])
                        weather.save()
                        print "Stored Weather info for " + loc + "\'s " + att + " for Year/Month : " + result[i][0] + "/" + result[7][j] + " as : " + result[i][j]