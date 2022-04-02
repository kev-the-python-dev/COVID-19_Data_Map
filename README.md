<pre><h1>COVID-19 Stats Tracker</h1>

<h2>Objectives:</h2>
*Display current Covid-19 cases, deaths, vaccinations completed.*

<h2>The Big Steps:</h2>
1. <strong>Download data from csse-covid-19 github repository.</strong><br></br>
    i. use 'raw' github link<br></br>
2. <strong>Access csv data from csse-covid-19</strong><br></br>
    i.  csv module required<br></br>
3.<strong>Transform/parse csv data into JSON (for easier reading via front-end)</strong><br></br>
    i. json module required<br></br>
    ii. create custom function to convert csv to json<br></br>
    iii. remove keys (columns) that are irrelevant to final data output<br></br>
4. <strong>Store data into database</strong><br></br>
    i. By storing data, we don't need to parse it everytime.<br></br>
    ii. json dump to convert json object into a json string that can be inserted in a text field in mysql.<br></br>
    iii. Using Django, export JSON data to MySQL database.<br></br>
5. <strong>Populate the stored data onto map (example use GeoJSON)</strong><br></br>
    i. geojson module required<br></br>
    ii. Take input from database, prepare the coords into GeoJSON format --> front-end framework can call this end-point while doing map implementation.<br></br>

---- Time for Front-end ----
1. <strong>React.js and redux</strong>
2. <strong>Populate coordinates using Mapbox (Source-Layer)</strong>


Notes:
1. *JHU CSSE updates data daily (23:59) UTC time. This will need to be synced to apps backend (aka update tables daily)*
2. *All data will be served via interactive map*
</pre>
