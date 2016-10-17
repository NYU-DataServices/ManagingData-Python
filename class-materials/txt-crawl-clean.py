#import the right Python libraries to complete our requests
#the library to grab URLs and data from webpages
import requests

#reads in the URL we want to scrape from
for line in requests.get('http://bit.ly/2dfjvCC').text.splitlines():
    #strips away white space from the beginning and end of a string -- can strip out other things if we want
    print(line.strip())
