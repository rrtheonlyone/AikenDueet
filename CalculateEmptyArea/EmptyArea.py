def circle(sha, rad):
    


def rectangle(sha, shadim):
    if (sha[0] > con[0]):
        dx = min(condim[0] - sha[0] + con[0], shadim[0])
    else:
        dx = min(shadim[0] - con[0] + sha[0], condim[0])
    if (sha[1] > con[1]):
        dy = min(condim[1] - sha[1] + con[1], shadim[1])
    else:
        dy = min(shadim[1] - con[1] + sha[1], condim[1])
    return condim[0] * condim[1] - dx*dy

ph = raw_input()
con = [int(x) for x in ph.split()] #Container Coordinates
ph = raw_input()
condim = [int(x) for x in ph.split()] #Height and width

t = raw_input() #Is the shape of child container

if t == "square":
    ph = raw_input()
    c = [int(x) for x in ph.split()] #Container Coordinates
    ph = int(raw_input())
    cp = [ph, ph] #Height and width
    print rectangle(c, cp)

elif t == "rectangle":
    ph = raw_input()
    c = [int(x) for x in ph.split()] #Container Coordinates
    ph = raw_input()
    cp = [int(x) for x in ph.split()] #Height and width
    print rectangle(c, cp)

elif t == "circle":
    ph = raw_input()
    c = [int(x) for x in ph.split()] #Container Coordinates
    ph = int(raw_input())
    print circle(c, ph)

else:
    print "Non type"

