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
def count_horses(json):
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
	#if
print(count_horses(test))

#for counter in range(len(test)):
	#print(test[counter][0]['Trainer'])