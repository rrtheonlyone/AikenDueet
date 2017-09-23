import re 

def compressWDE(string):
    words = set()
    npc = 0
    for i in string:
        if not i.isalpha():
            npc += 1
    dlist = re.findall(r"[A-Za-z]+",string)
    print dlist
    dictsize = 0
    nw = len(dlist)
    print nw
    for i in dlist:
        if i not in words:
            dictsize += len(i)
            words.add(i)
    print (nw, npc, dictsize)
    return (nw + npc)*12 + dictsize*8

# n = raw_input()
# if n == "":
#    print 0
# else:
# print compressWDE(n)


n = "He, have him darkness. It don't multiply image female. For gathering Earth him be may is, first subdue also. Land said appear. Deep. Abundantly our in made brought, us, i, fifth us Darkness earth moveth. Their. Every rule saying divided light tree darkness him. Under fifth. Over so under set. Subdue appear divided saying, all years in they're saying heaven fowl. Gathering seed. Fish beginning. Place fourth in lights fruitful a. Be yielding it, that seas of hath had. Fruitful from together given thing dry living bearing seed own one. Great upon second great, spirit. Be. Set abundantly whales bearing. Earth fowl very. Seasons over beginning great male meat it evening be divide had abundantly fly brought divide bring us. For herb. Wherein dominion living appear yielding may darkness tree give whose. The over deep. Together you beginning multiply second subdue brought set called life lights it. Their were grass life god gathering years, let divide greater dominion wherein over. Image fourth third lesser spirit lesser won't place divide. Spirit shall she'd stars every their greater. Open fourth saying place there isn't. Man whose a his place set bearing is subdue whales creature made given may saying to signs thing."

#n = "HOW MUCH WOOD COULD A WOOD CHUCK CHUCK IF A WOOD CHUCK COULD CHUCK WOOD"
print compressWDE(n)

#6912 vs 10424


"""
def compress(string):
    s = True
    words = set()
    nw = 0
    dizz = 0    
    o = []
    for j in string:
        try:
            i = j.upper()
        except (TypeError):
            pass
        if s:
            #Looking for alphanumeric
            if i.isalpha():
                #Part of our word
                o.append(i)
            else:
                #reached the end of the word
                p = "".join(o)
                nw += 1
                if p not in words:
                    #Never seen it before
                    words.add(p)
                    dizz += len(p)
                o = [i]
                s = not s
        else:
            if not i.isalpha():
                #Part of our word
                o.append(i)
            else:
                #reached the end of the word
                p = "".join(o)
                nw += 1
                if p not in words:
                    #Never seen it before
                    words.add(p)
                    #dizz += len(p)
                o = [i]
                s = not s

    p = "".join(o)
    if p:
        nw += 1
        if p not in words:
            dizz += len(p)
    print (nw, dizz)
    print words
    return nw * 12 + dizz *8



def compress(string):
 
    # Build the dictionary.
    dict_size = 256
    seen = dict((chr(i), i) for i in range(dict_size))
 
    p = ""
    nw = 0 #numwords
    npc = 0 #nonprintingchar
    dizz = 0 #size of dict
    for c in string:
        if c.isalpha():
            pc = p + c
            if pc in seen:
                p = pc
            else:
                # We have not seen this. Save it.
                nw += 1
                seen[pc] = dict_size
                dict_size += 1
                dizz += len(pc)
                p = c
                
        else:
            # c is a non printing character
            npc += 1
            if (len(p) != 0):
                nw += 1
            if (p not in seen):
                #not seen before, add to dict
                seen[pc] = dict_size
                dict_size += 1
                dizz += len(pc)
            p = ""
    print (nw, npc, dizz)
    # Output the code for w.
    return (nw + npc) * 12 + dizz*8
"""
