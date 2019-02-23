# given a string , return a string where for every charecter in the original there are three charecters


def threetimes(st):
    x = [i*3 for i in st]
    return "".join(x)


print(threetimes("mississippi"))
