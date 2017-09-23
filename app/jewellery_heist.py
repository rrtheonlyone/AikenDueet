def fakeknapsack(s, t):
    q = []
    o = 0
    for i in s:
        w = float(i["weight"])
        v = i["value"]
        q.append((v/w, w))
    q.sort()
    q.reverse()
    g = len(q)
    b = 0
    while t > 0:
        if b < g:
            d = q[b]
            l = min(t, d[1])
            o += l*d[0]
            t -= l
            b += 1
        else:
            break 

    return int(o)