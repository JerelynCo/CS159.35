Data where she scraped from: http://mmdatraffic.interaksyon.com/line-view-commonwealth.php
Data scraped: http://penoy.admu.edu.ph/~reina/
Uname: reina
PW: qu33n
You can download the data scraped through the use of wget. 
wget: wget -r --no-parent --reject=index.html --user=reina --password=qu33n http://penoy.admu.edu.ph/~reina/


Package: Beautiful soup package
	Save in the same folder where your script is.
	The script extracts the html file from the URL provided, then beautiful soup parses the html file by locating the HTML/CSS tags.

Next time: Do a time series graph from the data provided. 

CSV format:
year, month, day, hr, qtr, lineNum, stnNum, status, nStations
2014, 7-12, 1-31, 00-24, 1-4, 0-8, 0-nStations, 0-2, 0-2


