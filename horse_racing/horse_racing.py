import json
import operator
with open('horse_racing.json', 'r') as outfile:
	test = json.load(outfile)

print(len(test))
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
		print(horse_name + ' ' + jockey_name + ' ' + placing + ' ' + trainer)
		if horse_name in horse_lst:
			horse_lst[horse_name] += 1
		else: 
				horse_lst.update({horse_name:1})

	return max(horse_lst, key = horse_lst.get)
#Return the best Jockey
def best_jockey(json):
	jockey_lst = {}
	for horse in range(len(test)):
		jockey_name = test[horse]['jockeycode']
		if jockey_name in jockey_lst:
			jockey_lst[jockey_name] += 1
		else: 
			jockey_lst.update({jockey_name:1})

	return max(jockey_lst, key = jockey_lst.get)
#Return the best trainer
def best_trainer(json):
	trainer_lst = {}

	for horse in range(len(test)):
		trainer_name = test[horse]['Trainer']

		trainer = test[horse]['Trainer']
		if trainer_name in trainer_lst:
			trainer_lst[trainer_name] += 1
		else: 
			trainer_lst.update({trainer_name:1})

	return max(trainer_lst, key = trainer_lst.get)
print(best_jockey(test))
print(best_horses(test))
print(best_trainer(test))

#for counter in range(len(test)):
	#print(test[counter][0]['Trainer'])