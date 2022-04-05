import requests
from os import getcwd
import datetime 
import json
import csv
from pprint import pprint
'''COVID-19 data is acquired from John Hopkins University's github where they update the data
on a nearly daily basis

url = "https://raw.githubusercontent.com/kevin-douglas/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports_us/03-29-2022.csv"
'''
directory = getcwd()

#print(f'directory: {directory}')
filename = directory + '/cov-data.csv'
#print(f'filename: {filename}')
#r = requests.get(url)

#with open(filename, 'wb') as f:
#    f.write(r.content)

# Parsing the data'''
def csvToJson(csvFilePath, jsonFilePath):
    cov_data = {}

    with open(csvFilePath, encoding='utf-8') as csv_to_json:
        csvReader = csv.DictReader(csv_to_json)

        for rows in csvReader:
            key = rows['id']
            cov_data[key] = rows
    with open(jsonFilePath, 'w', encoding='utf-8') as json_file:
        json_file.write(json.dumps(cov_data, indent=4))

json_file_path = directory + '/cov_data.json'
#print(f'json file path: {json_file_path}')

csvToJson(filename,json_file_path)




