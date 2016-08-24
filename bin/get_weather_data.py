import sys

sys.path.append("/Users/vasu/projects/weather_data_management/lib/")

import WDM.metoffice

from WDM.parse_html import parse
from WDM.metoffice import met_data


base_url = "http://datapoint.metoffice.gov.uk/public/data/"
resource = "val/wxfcs/all/xml/3840?res=3hourly&key="
key = "270ea5ad-917a-40fc-a9d9-c5f659cf1f77"

Locations=['UK','England','Wales','Scotland']
Attr=['Tmax','Tmin','Tmean','Sunshine','Rainfall']

data = met_data(key)

for loc in Locations:
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
                    print result[i][0] + " : " + result[7][j] +  " = " + result[i][j]