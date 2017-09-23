def fakeknapsack(s, t):
    q = []
    o = 0
    for i in s:
        w = float(i["weight"])
        v = i["value"]
        if w == 0:
            o += v
        else:
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

    return o


pp = [
  {"weight": 1, "value": 200},
  {"weight": 3, "value": 240},
  {"weight": 5, "value": 150},
  {"weight": 2, "value": 140}
  ]

ppp = 5999

print fakeknapsack (pp ,ppp)

# s is a list of dicts of weight and value
