# import the right Python libraries to complete our requests
import io
# the library to grab URLs and data from webpages
import requests
# the library that lets us write and read CSVs
import csv

# put the text file into an array
lines = requests.get('http://bit.ly/2dfjvCC').text.splitlines()

# On Python 2, this is where we declare where we want to write our file to
#output_file = open('/home/vicky/Downloads/news1.csv', 'wb')

# On Python 3, use:
output_file = open('/PATH TO FILE/news.csv', 'w', encoding = 'utf8', newline='')

# this creates our writer, which will do all our heavy lifting. We give it the name of the output file & the dialect, meaning this will create a file readable by Excel
writer = csv.writer(output_file, dialect='excel')

# I want to add headers to the CSV, since there aren't any in our txt file
headers = ['Title', 'Link', 'Date', 'Tags', 'Description']

# this writes the row of headers, so each of of these will be a cell in a row
writer.writerow(headers)

# we have to go through lines and take the first five of each, write those to a row, and continue, so this will be our guide through the lines
line_iterator = iter(lines)

# while there are lines
while True:
    try:
        row = []
        #put five lines into the row array
        for _ in range(5):
            item = next(line_iterator)
            #item = item.encode('utf-8') # use only with Python 2; convert to utf-8 for the output
            row.append(item)
        #write those five lines across a row
        writer.writerow(row)
        #iterate over the two blank lines in our text file
        next(line_iterator)
        next(line_iterator)
    #stop the interation when there is nothing left!
    except StopIteration:
        break
