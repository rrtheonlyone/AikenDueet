import collections

statid = {}
destination = raw_input()
lst = [{"name": "Punggol","passengers": 80,"connections": [{"station": "Sengkang","line": "purple"}]}, {"name": "Sengkang","passengers": 40,"connections": [{"station": "Punggol","line": "purple"}, {"station": "Serangoon","line": "purple"}]}, {"name": "Serangoon","passengers": 40,"connections": [{"station": "LittleIndia","line": "purple"}, {"station": "Sengkang","line": "purple"}, {"station": "PayaLebar","line": "orange"}, {"station": "Bishan","line": "orange"}]}, {"name": "LittleIndia","passengers": 40,"connections": [{"station": "Serangoon","line": "purple"}, {"station": "DhobyGhaut","line": "purple"},]}, {"name": "DhobyGhaut","passengers": 20,"connections": [{"station": "LittleIndia","line": "purple"}, {"station": "HarbourFront","line": "purple"}, {"station": "Somerset","line": "red"}, {"station": "MarinaBay","line": "red"}, {"station": "Esplanade","line": "orange"}]}, {"name": "HarbourFront","passengers": 90,"connections": [{"station": "DhobyGhaut","line": "purple"}]}, {"name": "Somerset","passengers": 0,"connections": [{"station": "DhobyGhaut","line": "red"}, {"station": "Orchard","line": "red"}]}, {"name": "Orchard","passengers": 30,"connections": [{"station": "Somerset","line": "red"}, {"station": "Novena","line": "red"}]}, {"name": "Novena","passengers": 10,"connections": [{"station": "Orchard","line": "red"}, {"station": "Bishan","line": "red"}]}, {"name": "Bishan","passengers": 20,"connections": [{"station": "Novena","line": "red"}, {"station": "Woodlands","line": "red"}, {"station": "Serangoon","line": "orange"}]}, {"name": "Woodlands","passengers": 40,"connections": [{"station": "Bishan","line": "red"}]}, {"name": "MarinaBay","passengers": 100,"connections": [{"station": "DhobyGhaut","line": "red"}]}, {"name": "Esplanade","passengers": 0,"connections": [{"station": "DhobyGhaut","line": "orange"}, {"station": "PayaLebar","line": "orange"}]}, {"name": "PayaLebar","passengers": 75,"connections": [{"station": "Esplanade","line": "orange"}, {"station": "Serangoon","line": "orange"}]}]
## Gotta get rid of the hard code next time

def busybody(destination, lst):

    def DFS():
        if not dfs:
            return 0
        print dfs.popleft()


    statid = {}
    dictcount = 0
    adjlist = {}

    for i in lst:
        print i
        statname = i["name"]
        try:
            currid = statid[statname]
        except (KeyError):
            statid[statname] = dictcount
            currid = dictcount
            dictcount += 1
        output = set()
        for j in i["connections"]:
            statname = j["station"]
            try:
                con = statid[statname]
            except (KeyError):
                statid[statname] = dictcount
                con = dictcount
                dictcount += 1
            output.add(con)
        adjlist[currid] = output

    dfs = collections.deque()
    dfs.append(statid[destination])
    DFS()
    return adjlist



print busybody(destination, lst)

"""
Input format: busybody(destination, lst)
Destination: Destination Station Name
lst: List of dicts of json shit
"""

