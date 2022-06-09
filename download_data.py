import requests
from os import getcwd, remove, path
import shutil
import datetime
import csv, json

# External scripts required to convert original file into correct format for GeoDjango
import json_to_geojson, json_str_to_float

# First we check today's date, if not valid, we check previous date and so on.
today = datetime.date.today()
day_format = "%m-%d-%Y"
today_formatted = today.strftime(day_format)
 
url = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports_us/' + today_formatted + '.csv'
directory = getcwd()
filename = directory + '/cov-data.csv'

# Beginning Connection
try:
    r = requests.get(url)
    print(f'Downloading data from {url}.')

except requests.exceptions.Timeout as err:
    print(f'\n{err}\n')

# Checks if today's date contains any COVID-19 data
try:
    r.raise_for_status()
    print(r.raise_for_status())

# An error at this step indicates the URL for today's date is not active and will thus work backwards
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

# Store downloaded content into csv file
with open(filename, 'wb') as f:
    f.write(r.content)

# Conversion of CSV file (includes removal of unnecessary data) to JSON.
def csvToJson(csvFilePath, jsonFilePath):
    cov_data = []

    with open(csvFilePath) as infd, open('reformatted_covid_data.csv', 'w') as outfd:
        reader = csv.reader(infd)
        writer = csv.writer(outfd)

        # Original .csv has column named "Long_" and Django can't parse that correctly. So we are going to rename the "Long_" column to "Long".

        header = next(reader)
        header[4] = 'Long'

        # Some data is incomplete so removing 'blank' data
        writer.writerow((header[0], header[2], header[3], header[4], header[5], header[6], header[10], header[11]))
        for row in reader:
            writer.writerow((row[0], row[2], row[3], row[4], row[5], row[6], row[10], row[11]))

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
        print('JSON file created. Beginning conversion to GeoJSON.')

def file_removal(file1, file2, file3):
    print('Removing temporary files the original "download_data.py" script created.')
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
