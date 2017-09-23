import json
from collections import deque
import itertools
import re
with open('horse_racing.json', 'r') as outfile:
	test = json.load(outfile)

def jockey_name_and_placing(json):
	jockey_lst = []
	for horse in range(len(test)):
		
		jockey_name = test[horse]['jockeycode']
		race_placing = test[horse]['Placing']
		race_number = test[horse]['raceno']
		trainer = test[horse]['Trainer']
		horse_name = test[horse]['Horse']

		day_of_race = daytime_to_int(test[horse]['racedate'])

		#Identify Horse racedateces which occur within the same day
		#.split(" ")[1]	
		#race_number = re.sub(r'([0-9])', "",race_number)
		jockey_dict = {"pos": int(race_placing), "date":day_of_race, "joc":str(jockey_name),"race": int(race_number), 
						"horse":horse_name, "train":str(trainer)}
		jockey_lst.append(jockey_dict)
	return jockey_lst

#Lists and tuples 

def daytime_to_int(date):
	remove_dash = date.split("-")
	result = remove_dash[0] + remove_dash[1] +remove_dash[2]
	return int(result)



filtered_tuples = jockey_name_and_placing(test)
print(jockey_name_and_placing(filtered_tuples))