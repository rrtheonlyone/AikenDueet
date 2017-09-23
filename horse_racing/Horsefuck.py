mm = #Joel be working on this now.

def joel(json):
    def daytime_to_int(date):
    	remove_dash = date.split("-")
    	return int("".join(remove_dash))

	jockey_lst = []
	for i in range(len(json)):
		
		jockey_name = json[i]['jockeycode']
		race_placing = json[i]['Placing']
		race_number = json[i]['raceno']
		trainer = json[i]['Trainer']
		horse_name = json[i]['Horse']
		day_of_race = daytime_to_int(json[i]['racedate'])

		jockey_dict = {"pos": int(race_placing), 
                       "date": day_of_race, 
                       "joc": str(jockey_name),
                       "race": int(race_number), 
					   "horse": str(horse_name), 
                       "train": str(trainer)
                       }
		jockey_lst.append(jockey_dict)
	return jockey_lst

def question1(n):
    ho = {}
    jo = {}
    tr = {}
    for i in n:
        if i["pos"] = 1:
            bho = i["horse"]
            bjo = i["joc"]
            btr = i["train"]
            try:
                ho[bho] += 1
            except (KeyError):
                ho[bho] = 1
            try:
                jo[bjo] += 1
            except (KeyError):
                jo[bjo] = 1
            try:
                tr[btr] += 1
            except (KeyError):
                tr[btr] = 1

    a = -1
    for key, value in ho.items():
        if value > a:
            a = value
            bho = key
    a = -1
    for key, value in jo.items():
        if value > a:
            a = value
            bjo = key
    a = -1
    for key, value in tr.items():
        if value > a:
            a = value
            btr = key
    return {"horse":bho, "jockey":bjo, "trainer":btr}
        
def question2(n):
    combi = {}
    for i in n:
        ppl = i["pos"]
        if i["pos"] < 3:
            bho = i["horse"]
            bjo = i["joc"]
            btr = i["train"]
            tupl = (bho, bjo, btr)
            try:
                combi[tupl] += -1 + 2**(4-ppl)
            except (KeyError):
                combi[tupl] += -1 + 2**(4-ppl)

    a = -1
    for key, value in tr.items():
        if value > a:
            a = value
            tupl = key
    
    return {"horse":tupl[0], "jockey":tupl[1], "trainer":tupl[2]}

def mondieu(day_records):
    # ans is the final output of the method
    ans = dict()
    # candidate_dict stores candidate answers
    candidate_dict = dict()

    for i in range(len(day_records)):
        day = day_records[i]
        day_list = []

        # Check each consecutive triple in the day
        for joc0, joc1, joc2 in zip(day, day[1:], day[2:]):
            # Key used to identify a triple
            key = (joc0["joc"], joc1["joc"], joc2["joc"])

            # If the key exists in the candidate dict, update its frequency
            if key in candidate_dict:
                frequency = 1 + candidate_dict[key]
                # If frequency is met, add to the answer
                if frequency == 3:
                    ans[key] = (key, i)
                else:
                    day_list.append((key, frequency))
            # Else, create a new entry
            else:
                day_list.append((key, 1))

        # Transfer contents from day_list to candidate_dict
        # This gets rid of values that did not appear in the day
        candidate_dict.clear()
        for entry in day_list:
            key = entry[0]
            candidate_dict[key] = entry[1]

    output = []
    for value in ans.values():
        jockeys = list(value[0])
        dates = []
        races = []

        for i in range(value[1] - 2, value[1] + 1):
            arb_entry = day_records[i][0]
            dates.append(arb_entry["date"])
            races.append(arb_entry["race"])

        output.append({"jockeys": jockeys, "date": dates, "races": races})

    return output

def redates(lstrace, lstdate):
    output = []
    for i in range (3):
        r = lstrace[i]
        d = lstdate[i]
        output.append(str(d[0:4]) + "-" + str(d[5:6]) + "-" + str(d[7:8]) + ":" + str(r))
    return output

def question3(n):
    new = sorted(n, key=lambda k: k['date'])
    newer = []
    o = [new[0]]
    curr = new[0]["date"]
    for i in range(1, len(new)):
        if new[i]["date"] > curr:
            #Newday
            newer.append(o)
            o = []
        else:
            o.append(new[i])
    newer.append(o)
    new = [] #The Correct
    for i in newer:
        new.append(sorted(n, key=lambda k: k['race']))
    dayton = []    
    for i in new:
        for j in i:
            dayton.append((j[0]["date"], j[0]["race"]))
    outsh = mondieu(new)
    output = []
    for i in oursh:
        rd = redates(i["races"], i["date"])
        output.append({"jockeys": [i["joc"], i["joc"], i["joc"]], 
                       "races": rd})
    return output
                    
def horsefuck(lst):
    #input is a list of dictionaries.
    #"jock", "pos", "train", "date", "horse", "race"  
    processed = joel(lst)
    mm.extend(processed)
    return {"q1": question1(mm), "q2": question2(mm), "q3": question3(mm)}
