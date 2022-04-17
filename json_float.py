import json
json_file = 'geocovdata.json'

with open(json_file) as f:
    json_data = json.load(f)
    for feature in json_data['features']:
        coordinates = feature['geometry']['coordinates']
        feature['geometry']['coordinates'] = [float(coord) for coord in coordinates]
#Remove "Princess" states
with open(json_file, 'w') as f:
    json.dump(json_data, f, indent=4)
