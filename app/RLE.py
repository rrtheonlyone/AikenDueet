import math

def compress(string):
    curr = ""
    output = 0
    count = 0
    for i in string:
        if curr == i:
            count += 1
        else:
            output += 1 + math.ceil(math.log10(count + 1))
            count = 0
    output += count
    print output *8

n = raw_input()
print compress(n)
# Method call
# print(decode(encode("RRRRRRTTTTYYYULLL")))
# decode([('a', 5), ('h', 6), ('m', 7), ('u', 1), ('i', 7), ('a', 6)])
