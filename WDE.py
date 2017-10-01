import re 

def compressWDE(string):
    # print(string)
    words = set()
    npc = 1
    for i in range(len(string)):
        if not string[i].isalpha():
            npc += 1
            if (i > 1 and not string[i-1].isalpha()):
                npc+=1 
    dlist = re.findall(r"[A-Za-z]+",string)
    # print dlist
    dictsize = 0
    nw = len(dlist)
    # print nw
    for i in dlist:
        if i not in words:
            dictsize += len(i)
            words.add(i)
    # print (nw, npc, dictsize)
    print((nw + npc)*12 + dictsize*8)
    return (nw + npc)*12 + dictsize*8


# n = raw_hiinput()
# if n == "":
#    print 0
# else:
# print compressWDE(n)
