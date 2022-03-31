#COVID-19 Stats Tracker

Objectives:
Display current Covid-19 cases, deaths, vaccinations completed.

The Big Steps:
1. Access csv data from csse-covid-19
    i.  csv module required
2. Transform/parse csv data into JSON (for easier reading via front-end)
    i. json module required
    ii. create custom function to convert csv to json
    iii. remove keys (columns) that are irrelevant to final data output 
3. Store data into database
    i. By storing data, we don't need to parse it everytime.
    ii. json dump to convert json object into a json string that can be inserted in a tet field in mysql.
    iii. Using Django, export JSON data to MySQL database.
4. Populate the stored data onto map (example use GeoJSON)
    i. geojson module required
    i. Take input from database, prepare the coords into GeoJSON format --> front-end framework can call this end-point while doing map implementation. 

---- Time for Front-end ----
1. React.js and redux
2. Populate coordinates using Mapbox (Source-Layer)


Notes:
1. JHU CSSE updates data daily (23:59) UTC time. This will need to be synced to apps backend (aka update tables daily)
2. All data will be served via interactive map
