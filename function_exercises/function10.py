# returns the sum of the numbers in the array,
# except ignore sections of nembers starting with a 6 and extending to the next 9
#   (every 6 will be followed by atleast one 9) return 0 for no numbers

# [1,3,5] --> 9
# [4,5,6,7,8,9] --> 9
# [2,1,6,9,11] --> 14
# [4,5,6,7,8] --> 30


# loop over list
#   if 6 found:
#       check where is next 9
#       set index to 9's position
#       loop from 9,s position and add number to sum (or skip all numbers to 9,s position)
#   if 6 not found (else):
#    add number to sum


def sum_69(lst):
    sume = 0
    index = -1
    c = 0
    for i in lst:
        if lst.index(i, c) > index:
            if i == 6:
                index = lst.index(9, c)

            else:
                sume += i
        c += 1
    return sume


print(sum_69([1, 6, 9, 6, 9, 9, 2, 3, 9, 2, 8]))

## now if there is no 9 after 6 ##


# loop over list
#   if 6 found:
#       check where is next 9
#       if 9 found:
#           set index to 9's position
#           loop from 9,s position and add (or skip all numbers to 9,s position)
#        if 9 not found (else):
#           add  to sum from 6's position
#   if 6 not found (else):
#   add number to sum


def sum1_69(lst):
    sume = 0
    index = -1
    c = 0
    for i in lst:
        if lst.index(i, c) > index:
            if i == 6:
                if lst[c:].count(9) > 0:
                    index = lst.index(9, c)
                else:
                    sume += i
            else:
                sume += i
        c += 1
    return sume


print(sum1_69([1, 6, 9, 6, 9, 9, 2, 3, 9, 2, 6, 8]))
