#import the right Python libraries to complete our requests
#the library to grab URLs and data from webpages
import urllib.request

#reads in the URL we want to scrape from
for line in urllib.request.urlopen('http://bit.ly/2dfjvCC'): 
    # takes away the B at the beginning of each line (b stands for byte!)
    cleanLine = line.decode() 
    #strips away white space from the beginning and end of a string -- can strip out other things if we want
    print (cleanLine.strip()) 