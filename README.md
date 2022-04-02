<h1>COVID-19 Stats Tracker</h1>

<h2>Objectives:</h2>
*Display current Covid-19 cases, deaths, vaccinations completed.*

<h2>The Big Steps:</h2>
1. **Download data from csse-covid-19 github repository.**<br>
    i. use 'raw' github link<br> 
2. **Access csv data from csse-covid-19**<br>
    i.  csv module required<br>
3. **Transform/parse csv data into JSON (for easier reading via front-end)**<br>
    i. json module required<br>
    ii. create custom function to convert csv to json<br>
    iii. remove keys (columns) that are irrelevant to final data output<br> 
4. **Store data into database**<br>
    i. By storing data, we don't need to parse it everytime.<br>
    ii. json dump to convert json object into a json string that can be inserted in a text field in mysql.<br>
    iii. Using Django, export JSON data to MySQL database.<br>
5. **Populate the stored data onto map (example use GeoJSON)**<br>
    i. geojson module required<br>
    i. Take input from database, prepare the coords into GeoJSON format --> front-end framework can call this end-point while doing map implementation. <br>

---- Time for Front-end ----
1. **React.js and redux**
2. **Populate coordinates using Mapbox (Source-Layer)**


Notes:
1. *JHU CSSE updates data daily (23:59) UTC time. This will need to be synced to apps backend (aka update tables daily)*
2. *All data will be served via interactive map*
