def question3(day_records):
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

        output.append({"jockeys": jockeys, "dates": dates, "races": races})

    return output


# Testing
print(question3([[{"joc": "A", "date": 1, "race": 1}, {"joc": "B", "date": 1, "race": 1},
                  {"joc": "C", "date": 1, "race": 1}, {"joc": "D", "date": 1, "race": 1},
                  {"joc": "E", "date": 1, "race": 1}, {"joc": "F", "date": 1, "race": 1}],

                 [{"joc": "A", "date": 1, "race": 2}, {"joc": "B", "date": 1, "race": 2},
                  {"joc": "C", "date": 1, "race": 2}, {"joc": "D", "date": 1, "race": 2},
                  {"joc": "E", "date": 1, "race": 2}, {"joc": "B", "date": 1, "race": 2},
                  {"joc": "Q", "date": 1, "race": 2}],

                 [{"joc": "A", "date": 2, "race": 3}, {"joc": "C", "date": 2, "race": 3},
                  {"joc": "D", "date": 2, "race": 3}, {"joc": "E", "date": 2, "race": 3},
                  {"joc": "B", "date": 2, "race": 3}, {"joc": "F", "date": 2, "race": 3}],

                 [{"joc": "E", "date": 4, "race": 4}, {"joc": "B", "date": 4, "race": 4},
                  {"joc": "F", "date": 4, "race": 4}, {"joc": "A", "date": 4, "race": 4},
                  {"joc": "H", "date": 4, "race": 4}, {"joc": "T", "date": 4, "race": 4}],

                 [{"joc": "A", "date": 5, "race": 5}, {"joc": "D", "date": 5, "race": 5},
                  {"joc": "T", "date": 5, "race": 5}, {"joc": "E", "date": 5, "race": 5},
                  {"joc": "B", "date": 5, "race": 5}, {"joc": "F", "date": 5, "race": 5},
                  {"joc": "P", "date": 5, "race": 5}, {"joc": "M", "date": 5, "race": 5}]]))
