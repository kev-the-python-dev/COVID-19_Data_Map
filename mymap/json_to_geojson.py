from sys import argv
from os.path import exists
import json

'''To get get the original COVID-19 data to create actual map markers based on what state the data is for we needed to convert CSV --> JSON --> GeoJSON. The original script already transforms the csv data into json. This script's sole purpose is just to convert that JSON file into GeoJSON format for GeoDjango. ''' 

def conv_to_geo():
    
    print('Converting JSON into GeoJSON format.')

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
