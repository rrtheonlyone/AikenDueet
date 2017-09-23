def qsort (L):
    c = [0]*20001
    output = []
    for i in L:
        c[i+10000] += 1
    for i in range(20001):
        if c[i] != 0:
            temp = [i-10000]*c[i]
            output.extend(temp)
    print(c)
    return output


# L = [3,1,4,1,5,9,2,6,5,3,5,8,9,7,9]
# qsort(L)
# print L