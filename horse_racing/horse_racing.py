import json
from collections import deque
import itertools
import re
with open('horse_racing.json', 'r') as outfile:
	test = json.load(outfile)

#print(len(test))
jockey_wins = 0
horse_wins = 0
trainer_wins = 0
horse_lst = {}
trainer_lst = {}
jockey_lst = {}
def best_horses(json):
	horse_lst = {}
	for horse in range(len(test)):

		horse_name = test[horse]['Horse']
		jockey_name = test[horse]['jockeycode']
		placing = test[horse]['Placing']
		trainer = test[horse]['Trainer']


		#Print horse, jockey name , the placing and then the trainer of the horse 
		#print(horse_name + ' ' + jockey_name + ' ' + placing + ' ' + trainer)
		if horse_name in horse_lst and test[horse]['Placing'] == 1:
			horse_lst[horse_name] += 1
		else: 
			horse_lst.update({horse_name:1})
	return max(horse_lst, key = horse_lst.get)


#Return the best Jockey
def best_jockey(json):
	jockey_lst = {}
	for horse in range(len(test)):
		jockey_name = test[horse]['jockeycode']
		if jockey_name in jockey_lst and test[horse]['Placing'] == 1:
			jockey_lst[jockey_name] += 1
		else: 
			jockey_lst.update({jockey_name:1})

	return max(jockey_lst, key = jockey_lst.get)
#Return the best trainer
def jockey_lst(json):
	jockey_lst = {}
	for horse in range(len(test)):
		jockey_name = test[horse]['jockeycode']
		race_number = test[horse]['Placing']
		if jockey_name in jockey_lst:
			jockey_lst[jockey_name] += 1
		else: 
			jockey_lst.update({jockey_name:1})

	return jockey_lst


#Creates list with Jockey name ,placing and race number 
def jockey_name_and_placing(json):
	jockey_lst = []
	for horse in range(len(test)):
		jockey_name = test[horse]['jockeycode']
		race_placing = test[horse]['Placing']
		race_number = test[horse]['RaceIndex'].strip("RACE").split(' ')[1]

		#Identify Horse races which occur within the same day
	 	day_of_race = test[horse]['racedate']
		#.split(" ")[1]	
		#race_number = re.sub(r'([0-9])', "",race_number)
		jockey_lst.append((jockey_name, race_placing, race_number, day_of_race))

	return jockey_lst			
#Return the best trainer
def best_trainer(json):
	trainer_lst = {}

	for horse in range(len(test)):
		trainer_name = test[horse]['Trainer']

		trainer = test[horse]['Trainer']
		if trainer_name in trainer_lst and test[horse]['Placing'] == 1:
			trainer_lst[trainer_name] += 1
		else: 
			trainer_lst.update({trainer_name:1})

	return max(trainer_lst, key = trainer_lst.get)

def combination_of_horse(test):
	horse_lst = {}
	for horse in range(len(test)):

		horse_name = test[horse]['Horse']
		jockey_name = test[horse]['jockeycode']
		placing = test[horse]['Placing']
		trainer = test[horse]['Trainer']
		combination = horse_name + jockey_name +trainer


		#Print horse, jockey name , the placing and then the trainer of the horse 
		#print(horse_name + ' ' + jockey_name + ' ' + placing + ' ' + trainer)
		if horse_name in horse_lst and test[horse]['Placing'] == 1:
			horse_lst[combination] += 7
		elif horse_name in horse_lst and test[horse]['Placing'] == 2:
			horse_lst[combination] += 3
		elif horse_name in horse_lst and test[horse]['Placing'] == 3:
			horse_lst[combination] += 1
		else: 
			horse_lst.update({combination:0})

	return max(horse_lst, key = horse_lst.get)

#Returns horse races in order 




#Pass in a list sorted by day of race 

def three_seq_order(name_and_placing):	
	for counter in range(len(name_and_placing)):
		#print(name_and_placing[counter - 1][])
		if int(name_and_placing[counter][1]) == int(name_and_placing[counter - 1][1]) - 1  and int(name_and_placing[counter][1]) == int(name_and_placing[counter + 1][1] + 1) + 1:
				print(name_and_placing[counter][0])
				#Check the n + 1 th position and n-1th positio
				#Check the n + 2th position and the n - 1th position

#Generate list of tuples of jockey name and placing
jname = jockey_name_and_placing(test)
def sorted_list(test):
	other_test = sorted(jname, key = lambda jname: (jname[1], jname[2], jname[3]))
	return other_test
print(three_seq_order(sorted_list(jname)))
#print(three_seq_order(other_test))
#print(three_seq_order(other_test))
#for counter in range(len(test)):
	#print(test[counter][0]['Trainer'])		if int(name_and_placing[counter][1]) == int(name_and_placing[counter - 1][1]) - 1: 
		#if int(name_and_placing[counter][1]) == int(name_and_placing[counte		if int(name_and_placing[counter][1]) == int(name_and_placing[counter - 1][1]) - 1: 
		#if int(name_and_placing[counter][1]) == int(name_and_placing[counter - 1][1]) - 1: 
#r - 1][1]) - 1: 
