# write a function which takes a two word string and returns true if both words begin with same letter


def word_check(str):
    # for word in str.split():
    return str.lower().split()[0][0] == str.lower().split()[1][0]


print(word_check("fgf Fdf"))
