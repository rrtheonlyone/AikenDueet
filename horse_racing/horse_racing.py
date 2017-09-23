import json
with open('horse_racing.json', 'r') as outfile:
	print(json.load(outfile))