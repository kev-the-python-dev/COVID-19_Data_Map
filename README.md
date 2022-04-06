<pre><h1>COVID-19 Stats Tracker</h1>

<h2>Objectives:</h2>
*Display current Covid-19 cases, deaths, vaccinations completed.*

<h2>The Big Steps:</h2>
1. <strong>DONE</strong> - Download data from csse-covid-19 github repository.<br></br>
2. <strong>Done</strong> - Access csv data from csse-covid-19<br></br>
3.<strong>Done</strong> - Transform/parse csv data into JSON (for easier reading via front-end)<br></br>
4. <strong>Done</strong> - Store data into database<br></br>
To Do: <br><br>
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
