# write a function that counts the number of times a given pattern appears in a string, including overlap

# "hah", "hahahaha"  --> 3


def pattern_count(ptn, strg):
    count = 0
    while strg.find(ptn) != -1:
        i = strg.find(ptn)
        strg = strg[i+1:]
        count += 1
    return count


print(pattern_count("hah", "hahahah"))
