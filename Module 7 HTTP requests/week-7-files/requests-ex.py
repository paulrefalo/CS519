import requests
import json

url = "http://www.ncdc.noaa.gov/cdo-web/api/v2/data"

querystring = {"datasetid":"GHCND","locationid":"ZIP:97333","startdate":"2010-10-01","enddate":"2010-10-30","datatypeid":"PRCP","limit":"100","units":"standard"}
headers = {
    'token': "[your key here]",
    }

response = requests.get(url,headers=headers, params=querystring)

print(response.text)

results = json.loads(response.text)

print(results.keys())

for day in results["results"]:
	print("On " + day["date"] + 
		" there was " + str(day["value"]) + 
		"in of rain at station " + day["station"])
