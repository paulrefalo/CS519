import json

simpsons = {"Homer":{"age":40, "job":"Nuclear Engineer", "hair":"scarce"},
			"Marge":{"age":42, "job":"Housewife", "hair":"blue and tall"},
			"Lisa":{"age":8, "job":"Student", "hair":"star"},
			"Bart":{"age":10, "job":"Student", "hair":"spikey"},
			"Maggie":{"age":1, "job":"Baby", "hair":"star"},
			"ExampleArray":["foo", "bar", "baz"]}

f = open("simpsons-output.json",'w')
if f:
	f.write(json.dumps(simpsons))
	f.close()