# CS 519 assignment 7 - ISS.py "When can I see the ISS" by Paul ReFalo
# View | Tool Windows | Terminal
# python3 ISSrefactored.py "Portland, OR" 3

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

# get Request function takes url, headers, query and returns API response if successful
def getRequest(requestURL, requestHeaders, requestQueryString):
    error_count = 0
    success = False

    while not success and error_count < 3:
      #response = requests.request("GET", requestURL)
      getResponse = requests.get(requestURL, headers=requestHeaders, params=requestQueryString)  # get response
      if getResponse.status_code < 400:
        success = True
      else:
        print("===== API failed.  Retrying it now...standby. =====")
        error_count += 1

    if success:
        return getResponse
    else:
        print("Too many errors, giving up")
        sys.exit()

# use input from user to get Lat and Long of address
googleUrl = "https://maps.googleapis.com/maps/api/geocode/json"     # set up google url
googleQueryString = {"address":address}                             # config query string
googleHeaders = { }                                                 # no headers needed

googleResponse = getRequest(googleUrl, googleHeaders, googleQueryString)
googleResults = json.loads(googleResponse.text)  # use loads to get json text


for gr in googleResults["results"]:                     # loop and extract lat and long of address
    lat = gr["geometry"]["location"]["lat"]
    long = gr["geometry"]["location"]["lng"]

# use lat and long to get ISS viewing times
issUrl = "http://api.open-notify.org/iss-pass.json"     # set up ISS url
issHeaders = { }                                        # no headers needed
issQueryString = {"lat":lat, "lon":long, "n":n}         # config queryString

issResponse = getRequest(issUrl, issHeaders, issQueryString)
issResults = json.loads(issResponse.text)  # use loads to get json text

issResultsArray = []                    # set up array to hold ISS results
for issR in issResults["response"]:     # loop to get individual results
    duration = issR["duration"]         # extract duration in seconds
    risetime = issR["risetime"]         # extract risetime in seconds since epoch
    risetime = time.strftime('%a %b %d %H:%M:%S %Y', time.localtime(risetime)) # format time

    issResultsArray.append((duration, risetime)) # append to results array

print("From " + address + " you will be able to see the ISS on:")
for idx, e in enumerate(issResultsArray):       # loop to display results in proper format
    if idx >= n:                                # break if length(issResultsArray is larger than n,
        break                                   # this shouldn't happen or be needed (just in case)
    print(str(e[1]) + " for " + str(e[0]) + " seconds")     # print results


'''
Output demo:
MacBook-Pro:week-7-files paulrefalo$ python ISS.py "Santa Cruz, CA" 3
From Salem, OR you will be able to see the ISS on:
Sun Nov 19 19:57:16 2017 for 352 seconds
Sun Nov 19 21:30:39 2017 for 622 seconds
Sun Nov 19 23:07:01 2017 for 633 seconds

if API fails you might get:
===== API failed.  Retrying it now...standby. =====
===== API failed.  Retrying it now...standby. =====
From Salem, OR you will be able to see the ISS on:
Sun Nov 19 19:57:16 2017 for 352 seconds
Sun Nov 19 21:30:39 2017 for 622 seconds
Sun Nov 19 23:07:01 2017 for 633 seconds
'''