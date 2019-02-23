# write a function that capitalizes the first nd fourth letters of a name
#


def capitalize(name):
    return name.replace(name[0], name[0].upper(), 1).replace(name[3], name[3].upper(), 1)


print(capitalize("sanu p"))
