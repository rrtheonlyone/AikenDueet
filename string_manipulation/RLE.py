def encode(input_string):
    count = 1
    prev = ''
    lst = []
    output = '' 
    for character in input_string:
        if character != prev:
            if prev:
                entry = (prev,count)
                output = output + str(count) + str(prev)  
                lst.append(entry)
                #print lst
            count = 1
            prev = character
        else:
            count += 1
    else:
        entry = (character,count)
        lst.append(entry)
        output = output + str(count) + str(character)
    return output
 
 
def decode(lst):
    q = ""
    for character, count in lst:
        q += character * count
    return q
 
#Method call
print(encode("RRRRRRTTTTYYYULLL"))
decode([('a', 5), ('h', 6), ('m', 7), ('u', 1), ('i', 7), ('a', 6)])