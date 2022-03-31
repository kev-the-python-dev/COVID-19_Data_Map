#COVID-19 Stats Tracker

Objectives:
Display current Covid-19 cases, deaths, vaccinations completed.

The Big Steps:
1. Access csv data from csse-covid-19
3. Transform/parse csv data into JSON (for easier reading via front-end)
3. Store data into database
    i. By storing data, we don't need to parse it everytime.
4. Populate the stored data onto map (example use GeoJSON)
    i. Take input from database, prepare the coords into GeoJSON format --> front-end framework can call this end-point while doing map implementation. 

---- Time for Front-end ----
1. React.js and redux
2. Populate coordinates using Mapbox (Source-Layer)


Notes:
1. JHU CSSE updates data daily (23:59) UTC time. This will need to be synced to apps backend (aka update tables daily)
2. All data will be served via interactive map
