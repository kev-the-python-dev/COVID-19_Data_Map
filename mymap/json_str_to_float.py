import json

'''With our original we ran into an issue where the floating #'s were converted to string format. GeoJSON can not read this and map out location points (Long and Lat) without some kind of numerical value. This script fixes that issue. It is ran alongside the main script, so there is no need to touch/modify this.'''

def conv_to_float():
    
    print('Converting all number strings into integers & floats.')
    
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

