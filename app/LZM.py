def compress(string):
    """Compress a string to a list of output symbols."""
 
    # Build the dictionary.
    dict_size = 256
    seen = dict((chr(i), i) for i in range(dict_size))
 
    p = ""
    output = 0
    for c in string:
        pc = p + c
        if pc in seen:
            p = pc
        else:
            # We have not seen this. Output the stuff.
            output += 1
            seen[pc] = dict_size
            dict_size += 1
            p = c
 
    # Output the code for w.
    if p:
        output += 1
    return output * 12

# n = raw_input() #The input for the string will be here.
# print compress(n)
