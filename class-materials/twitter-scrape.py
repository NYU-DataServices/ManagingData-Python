#!/usr/bin/python
import tweepy
import datetime
import csv

# Authorize twitter with credentials (these are fake and won't work after class)
auth = tweepy.auth.OAuthHandler('', '')
auth.set_access_token('', '')

# get authorization
api = tweepy.API(auth)

# Open/Create a file to append data
csvFile = open('/PATH TO FILE/reprozipTweets.csv', 'a')

# Use csvWriter to write to a csv
csvWriter = csv.writer(csvFile)

# Add headers to our CSV file
headers = ['Date', 'Tweet', 'User', 'Link']

# this writes the row of headers, so each of of these will be a cell in a row
csvWriter.writerow(headers)

# for all the tweets in our search below
for tweet in tweepy.Cursor(api.search, 
                    q="reprozip", 
                    show_user = True,
                    since= datetime.datetime.now().date(), 
                    include_entities=True).items():
# Write a row to the csv file
    csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8'), tweet.user.screen_name, "https://twitter.com/" + str(tweet.user.screen_name) + "/status/" + str(tweet.id)])
# When all the tweets are grabbed, close the CSV file
csvFile.close()
