from sys import argv
from os.path import exists
#import simplejson as json
import json

script, in_file, out_file = argv

data = json.load(open(in_file, "r", encoding="utf-8"))

geojson = {
        "type": "FeatureCollection",
        "features": [
            {
                "type":"Feature",
                "geometry" : {
                    "type": "Point",
                    "coordinates" : [d["Long"],d["Lat"]],
                    },
                "properties" : d,
                } for d in  data]
            }

output = open(out_file, 'w', encoding="utf-8")
json.dump(geojson, output, indent=4)
output.close()
