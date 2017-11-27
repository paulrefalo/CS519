# CS 519 Refactoring assignment - ISSrefactored.py "When can I see the ISS" by Paul ReFalo

import sys
import requests
import json
from pprint import pprint
import time

# Global variables to hold lat and long
lat = 0
long = 0

address = sys.argv[1]   # address of location from user input
n = int(sys.argv[2])    # number of desired results

# use input from user to get Lat and Long of address
googleUrl = "https://maps.googleapis.com/maps/api/geocode/json"     # set up google url
googleQueryString = {"address":address}                             # config query string
googleHeaders = { }                                                 # no headers needed

googleAPI = False
for i in range(5):      # give API a few chances to succeed.  Abort script in unable to get response
    if googleAPI:
        break
    for attempt in range(5):
        try:
            response = requests.get(googleUrl, headers=googleHeaders, params=googleQueryString)  # get response
            googleResults = json.loads(response.text)  # use loads to get json text

            if googleResults["results"]:
                googleAPI = True
                break
        except ConnectionError:
            continue
        else:
            print("===== Google API failed.  Retrying it now...standby. =====")
            break
    else:
        print("Google geolocation failed.  Try script again or check connection.")
        sys.exit()

#print(response.text)


for gr in googleResults["results"]:                     # loop and extract lat and long of address
    lat = gr["geometry"]["location"]["lat"]
    long = gr["geometry"]["location"]["lng"]

# use lat and long to get ISS viewing times
issUrl = "http://api.open-notify.org/iss-pass.json"     # set up ISS url
issHeaders = { }                                        # no headers needed
issQueryString = {"lat":lat, "lon":long, "n":n}         # config queryString

issAPI = False
for i in range(5):      # give API a few chances to succeed.  Abort script in unable to get response
    if issAPI:
        break
    for attempt in range(5):
        try:
            issResponse = requests.get(issUrl, headers=issHeaders, params=issQueryString)  # get response
            issResults = json.loads(issResponse.text)  # use loads to get json text

            if issResults["response"]:
                issAPI = True
                break
        except ConnectionError:
            continue
        else:
            print("===== ISS API failed.  Retrying it now...standby.  =====")
            break
    else:
        print("ISS Api failed.  Try script again or check connection.")
        sys.exit()

#print(issResponse.text)

issResultsArray = []                    # set up array to hold ISS results
for issR in issResults["response"]:     # loop to get individual results
    duration = issR["duration"]         # extract duration in seconds
    risetime = issR["risetime"]         # extract risetime in seconds since epoch
    risetime = time.strftime('%a %b %d %H:%M:%S %Y', time.localtime(risetime)) # format time

    issResultsArray.append((duration, risetime)) # append to results array

print("You will be able to see the ISS on:")
for idx, e in enumerate(issResultsArray):       # loop to display results in proper format
    if idx >= n:                                # break if length(issResultsArray is larger than n,
        break                                   # this shouldn't happen or be needed (just in case)
    print(str(e[1]) + " for " + str(e[0]) + " seconds")     # print results



'''
Output demo:
MacBook-Pro:week-7-files paulrefalo$ python ISS.py "Santa Cruz, CA" 3
You will be able to see the ISS on:
Sat Nov 04 10:52:18 2017 for 625 seconds
Sat Nov 04 12:28:58 2017 for 582 seconds
Sun Nov 05 01:59:17 2017 for 103 seconds

if API fails you might get:
===== Google API failed.  Retrying it now...standby. =====
===== Google API failed.  Retrying it now...standby. =====
You will be able to see the ISS on:
Sat Nov 04 10:52:18 2017 for 625 seconds
Sat Nov 04 12:28:58 2017 for 582 seconds
Sun Nov 05 01:59:17 2017 for 103 seconds

'''