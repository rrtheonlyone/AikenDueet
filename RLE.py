import math

def compress1(string):
    curr = ""
    output = -1
    count = 1
    for i in string:
        if curr == i:
            count += 1
        else:
            if count == 1:
                output += 1
            else:
                output += 1 + math.ceil(math.log10(count+1))
            count = 1
            curr = i
    if count == 1:
        output += 1
    else:
        output += 1 + math.ceil(math.log10(count+1))
    return int(output * 8)

# n = raw_input()
# print compress(n)

# Method call
# print(decode(encode("RRRRRRTTTTYYYULLL")))
# decode([('a', 5), ('h', 6), ('m', 7), ('u', 1), ('i', 7), ('a', 6)])
