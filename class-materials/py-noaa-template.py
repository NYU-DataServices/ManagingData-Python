#!/usr/bin/python

import gzip
import pandas as pd
import urllib
import re
from IPython.display import display

baseurl = 'http://www1.ncdc.noaa.gov/pub/data/swdi/stormevents/csvfiles/'   #URL of NOAA directory.

fintable = pd.DataFrame()   #Creating an empty dataframe. Tables will be appended to this dataframe as they are opened.

html = urllib.request.urlopen(baseurl)     #Return the html from main directory page as an HTTP Response object

for i in html.readlines():  #Iterating through returned HTTPResponse object, one line at a time.
    line = i.decode('utf-8').lstrip()   # each line is a byte object, we want a string with no leading whitespace
    filename = re.findall(r'StormEvents_details-ftp_v1\.0_d\d{4}_c\d{8}\.csv\.gz', line) #match reg expression pattern and return matches as a list of strings
    if filename:                 #If the given line contains the match (i.e. returns True), execute the following
        yearurl = baseurl + filename[0]      #Add the matched pattern to the base URL to create path to sub table.
        yearfilezip = urllib.request.urlopen(yearurl)     #Read the gzip table file as an HTTP Response object
        yearfile = gzip.open(yearfilezip)                 #Read the HTTP Response object using gzip library, returning a file object
        table = pd.read_csv(yearfile, encoding='ISO-8859-1', low_memory=False)  #Read any unzipped table encoded in UTF-8 as a dataframe
        fintable = pd.concat([fintable, table])    #Append the dataframe to the final dataframe

#Display an abbreviated version of the table in the Notebook
display(fintable)
#Export a select few columns of the dataframe to a csv and save to desktop.
fintable.to_csv(r'PATH TO FILE/storm-events2.csv', encoding='utf-8', columns=["BEGIN_YEARMONTH", "EVENT_ID", "STATE", "STATE_FIPS", "CZ_FIPS", "CZ_NAME", "EVENT_TYPE", "DAMAGE_PROPERTY", "BEGIN_LAT", "BEGIN_LON"])


