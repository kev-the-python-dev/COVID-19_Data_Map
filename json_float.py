import json

def conv_to_float():
    file = 'geocovdata.json'
    with open(file) as f:
        json_data = json.load(f)
        for feature in json_data['features']:
            coordinates = feature['geometry']['coordinates']
            feature['geometry']['coordinates'] = [float(coord) for coord in coordinates]
    with open(file, 'w') as f:
        json.dump(json_data, f, indent=4)

if __name__ == '__main__':
    conv_to_float()

