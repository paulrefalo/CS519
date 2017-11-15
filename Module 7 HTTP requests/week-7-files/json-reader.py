import json

f = open("example.json")

if f:
	characters = json.loads(f.read())
	f.close()
	print(characters)
	print("The characters are")
	for c in characters["simpsons"]:
		print(c.keys()[0])
		print(c.keys()[0] + " is a " + c[c.keys()[0]]["job"])