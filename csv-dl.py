import requests
from os import getcwd, remove, path
import subprocess
import shutil
import datetime
import csv, json

# Required to convert original file into correct format for GeoDjango
import json_to_geojson, json_str_to_float

# First we check today's date, if not valid, we check previous date and so on.
today = datetime.date.today()
day_format = "%m-%d-%Y"
today_formatted = today.strftime(day_format)
 
url = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports_us/' + today_formatted + '.csv'
directory = getcwd()
filename = directory + '/cov-data.csv'
r = requests.get(url)

try:
    r.raise_for_status()
    print(r.raise_for_status())
except requests.exceptions.HTTPError as e:
    day_delta = datetime.timedelta(days=1)
    start_date = datetime.date.today()
    end_date = start_date - 30*day_delta
    
    for i in range((start_date - end_date).days):
        prev_date_search = start_date - i*day_delta
        prev_found_date = prev_date_search.strftime(day_format)
        url_2 = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports_us/' + prev_found_date + '.csv'
        r = requests.get(url_2)
        
        if r.status_code == 200:
            break

with open(filename, 'wb') as f:
    f.write(r.content)    

def csvToJson(csvFilePath, jsonFilePath):
    cov_data = []

    with open(csvFilePath) as infd, open('reformatted_covid_data.csv', 'w') as outfd:
        reader = csv.reader(infd)
        writer = csv.writer(outfd)

        # Original .csv has column named "Long_" and Django can't parse that correctly. So we are going to rename the "Long_" column to "Long".

        header = next(reader)
        header[4] = 'Long'

        writer.writerow(header)

        for row in reader:
            writer.writerow(row)

    new_csv = directory + '/reformatted_covid_data.csv'
   
    # Unfortunately the original data includes locations that aren't U.S. specific and breaks program. This removes those locations and once removed will write to a regular JSON file.
 
    with open(new_csv, encoding='utf-8') as csv_to_json:
        csvReader = csv.DictReader(csv_to_json)
        
        for rows in csvReader:
            if 'Princess' in rows['Province_State']:
                pass
            else:
                cov_data.append(rows)
    
    with open(jsonFilePath, 'w', encoding='utf-8') as json_file:
        json_file.write(json.dumps(cov_data, indent=4))

def file_removal(file1, file2, file3):
    remove(file1)
    remove(file2)
    remove(file3)

json_file_path = directory + '/cov_data.json'

if __name__ == '__main__':
    csvToJson(filename,json_file_path)
    json_to_geojson.conv_to_geo()
    json_str_to_float.conv_to_float()
    file_removal('./cov-data.csv', './reformatted_covid_data.csv', './cov_data.json')
    shutil.move('./geocovdata.json', './mymap/static/geocovdata.json')
