import requests
from os import getcwd
import subprocess
import datetime 
import csv, json
url = "https://raw.githubusercontent.com/kevin-douglas/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports_us/03-29-2022.csv"

directory = getcwd()

filename = directory + '/cov-data.csv'
r = requests.get(url)

with open(filename, 'wb') as f:
    f.write(r.content)    
    #COMMAND = '''awk -F, -v OFS=, 'NR==1 && $5=="Long_" {$5="Long"};1' cov-data.csv'''
    #subprocess.call(COMMAND, shell=True)
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
            cov_data.append(rows)
    
    with open(jsonFilePath, 'w', encoding='utf-8') as json_file:
        json_file.write(json.dumps(cov_data, indent=4))

json_file_path = directory + '/cov_data.json'

csvToJson(filename,json_file_path)



