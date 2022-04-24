import requests
from os import getcwd, remove, path
import subprocess
import shutil
import datetime
import csv, json

#python script imports
import json2geo, json_float

#Main Execution
today = datetime.date.today()
day_format = "%m-%d-%Y"
today_formatted = today.strftime(day_format)
 
url = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports_us/' + today_formatted + '.csv'
print(url)
directory = getcwd()
filename = directory + '/cov-data.csv'

r = requests.get(url)
try:
    r.raise_for_status()
    print(r.raise_for_status())
except requests.exceptions.HTTPError as e:
    print('error')
    day_delta = datetime.timedelta(days=1)
    start_date = datetime.date.today()
    end_date = start_date - 30*day_delta
    for i in range((start_date - end_date).days):
        new_date = start_date - i*day_delta
        new_date = new_date.strftime(day_format)
        url_2 = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports_us/' + new_date + '.csv'
        r = requests.get(url_2)
        if r.status_code == 200:
            print(f'{url_2} is valid')
            break

with open(filename, 'wb') as f:
    f.write(r.content)    
    COMMAND = '''awk -F, -v OFS=, 'NR==1 && $5=="Long_" {$5="Long"};1' cov-data.csv'''
    subprocess.call(COMMAND, shell=True)
# Parsing the data
def csvToJson(csvFilePath, jsonFilePath):
    cov_data = []

    # For renaming the Long_ column to Long (required for djano-import-export format)
    with open(csvFilePath) as infd, open('reformatted_covid_data.csv', 'w') as outfd:
        reader = csv.reader(infd)
        writer = csv.writer(outfd)

        header = next(reader)
        header[4] = 'Long'

        writer.writerow(header)

        for row in reader:
            writer.writerow(row)

    new_csv = directory + '/reformatted_covid_data.csv'
   # Convert .csv to JSON (list with nested dict)
    with open(new_csv, encoding='utf-8') as csv_to_json:
        csvReader = csv.DictReader(csv_to_json)
        
        for rows in csvReader:
            if 'Princess' in rows['Province_State']:
                pass
            else:
                cov_data.append(rows)
    
    with open(jsonFilePath, 'w', encoding='utf-8') as json_file:
        json_file.write(json.dumps(cov_data, indent=4))

json_file_path = directory + '/cov_data.json'

if __name__ == '__main__':
    csvToJson(filename,json_file_path)
    json2geo.conv_to_geo()
    json_float.conv_to_float()
    remove('./cov-data.csv')
    remove('./reformatted_covid_data.csv')
    remove('./cov_data.json')
    shutil.move('./geocovdata.json', './mymap/static/geocovdata.json')
