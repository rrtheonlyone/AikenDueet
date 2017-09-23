def question3(json_file):
    # ans is the final output of the method
    ans = dict()
    # candidate_dict stores candidate answers
    candidate_dict = dict()

    for day in json_file:
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
                    ans[key] = (joc0, joc1, joc2)
                else:
                    day_list.append(((joc0, joc1, joc2), frequency))
            # Else, create a new entry
            else:
                day_list.append(((joc0, joc1, joc2), 1))

        # Transfer contents from day_list to candidate_dict
        # This gets rid of values that did not appear in the day
        candidate_dict.clear()
        for entry in day_list:
            key = (entry[0][0]["joc"], entry[0][1]["joc"], entry[0][2]["joc"])
            candidate_dict[key] = entry[1]

    return ans.values()


# Testing
print(question3([[{"joc": "A"}, {"joc": "B"}, {"joc": "C"}, {"joc": "D"}, {"joc": "E"}, {"joc": "F"}],
                 [{"joc": "A"}, {"joc": "B"}, {"joc": "C"}, {"joc": "D"}, {"joc": "E"}, {"joc": "B"}, {"joc": "Q"}],
                 [{"joc": "A"}, {"joc": "C"}, {"joc": "D"}, {"joc": "E"}, {"joc": "B"}, {"joc": "F"}],
                 [{"joc": "E"}, {"joc": "B"}, {"joc": "F"}, {"joc": "A"}, {"joc": "H"}, {"joc": "T"}],
                 [{"joc": "A"}, {"joc": "D"}, {"joc": "T"}, {"joc": "E"}, {"joc": "B"}, {"joc": "F"}, {"joc": "P"},
                  {"joc": "M"}]]))
