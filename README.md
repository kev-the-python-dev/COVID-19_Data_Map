#COVID-19 Stats Tracker

Objectives:
Display current Covid-19 cases, deaths, vaccinations completed.

Steps:
1. Using the requests module, we access from COVIDActNow API:
	a. COVID confirmed cases, deaths, and recovered data.
	b. Filter this data by state.
2. Export the data into a csv object to be loaded into Pandas
	a. Rows: State
	b. Columns: Confirmed cases, deaths, & recovered.
3. Transform data into a dataframe using Pandas
4. Fine-tune Pandas in order to show (for speed) only the data requested
5. Plot the data using matplotlib (testing purposes before front end)
	a. When a user requests state information, the information is filtered into a separate data frame.  
6. Serve the information to end-user using Django (server), HTML/CSS
7. (Possibly use Javascript for front-end interactive aesthetics.
