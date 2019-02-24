## calculate the number of upper and lower charecter in a given string ##


def calc_upper_lower(st):

    low = 0
    hig = 0
    for i in st:
        if i.islower() == True and i.isalpha() == True:
            low += 1
        elif i.isalpha() == True:
            hig += 1

    return f"uppercase count= {hig} lowercase count= {low}"


print(calc_upper_lower("GiVen SitingG dJ"))
