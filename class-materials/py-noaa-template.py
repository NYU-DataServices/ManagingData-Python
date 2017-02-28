#!/usr/bin/python
import gzip
import io
import pandas as pd
import requests
import re
from IPython.display import display

baseurl = 'http://www1.ncdc.noaa.gov/pub/data/swdi/stormevents/csvfiles/'   #Shortened URL to NOAA base directory -- use this to be able to copy/paste the address above, but DO NOT REPLACE IT in the variable: https://goo.gl/gAevMH

fintable = pd.DataFrame()   #Creating an empty dataframe. Tables will be appended to this dataframe as they are opened.

html = requests.get(baseurl).text     #Return the html from main directory page as a string

for line in html.splitlines():  #Iterating through returned HTTPResponse object, one line at a time.
    line = line.lstrip()   # we want a string with no leading whitespace
    filename = re.findall(r'StormEvents_details-ftp_v1\.0_d\d{4}_c\d{8}\.csv\.gz', line) #match reg expression pattern and return matches as a list of strings
    if filename:                 #If there are matches in this line, execute the following
        yearurl = baseurl + filename[0]      #Add the matched pattern to the base URL to create path to sub table.
        yeardatagzip = requests.get(yearurl).content     #Get the table file
        yearfilegzip = io.BytesIO(yeardatagzip)
        yearfile = gzip.GzipFile(fileobj=yearfilegzip, mode='rb')
        table = pd.read_csv(yearfile, low_memory=False, encoding='iso-8859-15')  #Read the table as a dataframe
        fintable = pd.concat([fintable, table])    #Append the dataframe to the final dataframe

# Display an abbreviated version of the table in the Notebook
display(fintable)

# Export a select few columns of the dataframe to a csv
fintable.to_csv(r'/PATH TO FILE/storm-events2.csv', encoding='utf-8', columns=["BEGIN_YEARMONTH", "EVENT_ID", "STATE", "STATE_FIPS", "CZ_FIPS", "CZ_NAME", "EVENT_TYPE", "DAMAGE_PROPERTY", "BEGIN_LAT", "BEGIN_LON"])
