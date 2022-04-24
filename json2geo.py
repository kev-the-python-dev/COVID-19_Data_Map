from sys import argv
from os.path import exists
import json


def conv_to_geo():
    in_file= './cov_data.json'
    out_file = './geocovdata.json'

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

if __name__ == '__main__':
    conv_to_geo()
