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
    return lst
 
 
def decode(lst):
    q = 0 
    bit_length = 8  
    for character, counter in lst:
        if counter != 1: 
            q += 2 
            print(character)
        else :
            q+=1
    q = q * 8
    return q
 
#Method call
# print(decode(encode("RRRRRRTTTTYYYULLL")))
# decode([('a', 5), ('h', 6), ('m', 7), ('u', 1), ('i', 7), ('a', 6)])