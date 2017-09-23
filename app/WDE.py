import re 

def compressWDE(string):
    words = set()
    npc = 0
    for i in string:
        if not i.isalpha():
            npc += 1
    dlist = re.findall(r"\w+",string)
    dictsize = 0
    nw = len(dlist)
    for i in dlist:
        if i not in words:
            dictsize += len(i)
            words.add(i)
    return (nw + npc)*12 + dictsize*8


n = raw_input()
if n == "":
    print 0
else:
    print compressWDE(n)
