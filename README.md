<h1>COVID-19 Stats Tracker</h1>

<h2>Objectives:</h2>
*Display current Covid-19 cases, deaths, vaccinations completed.*

<h2>The Big Steps:</h2>
1. <em>Download data from csse-covid-19 github repository.<em><br></br>
    i. use 'raw' github link<br></br>
2. <em>Access csv data from csse-covid-19</em><br></br>
    i.  csv module required<br></br>
3. <em>Transform/parse csv data into JSON (for easier reading via front-end)</em><br></br>
    i. json module required<br></br>
    ii. create custom function to convert csv to json<br></br>
    iii. remove keys (columns) that are irrelevant to final data output<br></br>
4. <em>Store data into database</em><br></br>
    i. By storing data, we don't need to parse it everytime.<br></br>
    ii. json dump to convert json object into a json string that can be inserted in a text field in mysql.<br></br>
    iii. Using Django, export JSON data to MySQL database.<br></br>
5. <em>Populate the stored data onto map (example use GeoJSON)</em><br></br>
    i. geojson module required<br></br>
    ii. Take input from database, prepare the coords into GeoJSON format --> front-end framework can call this end-point while doing map implementation.<br></br>

---- Time for Front-end ----
1. <em>React.js and redux</em>
2. <em>Populate coordinates using Mapbox (Source-Layer)</em>


Notes:
1. *JHU CSSE updates data daily (23:59) UTC time. This will need to be synced to apps backend (aka update tables daily)*
2. *All data will be served via interactive map*
