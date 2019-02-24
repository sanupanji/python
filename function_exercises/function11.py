## write a function that takes in a list of integers and returns true if it contains 007 in order ##

# [1,2,30,33,0,0,7,35] -- > True
# [4,0,4,2,6,0,5,22,7,52,8] --> True
# [5,0,5,6,7,0,2,6,9] --> False

#############################
# loop over list
#   if 0 exist:
#       if next 0 exit:
#           if 7 exist:
#               return True
#   else:
#       return false


def check_007(lst):

    if lst.count(0) > 0:
        index1 = lst.index(0)
        if lst[index1+1:].count(0) > 0:
            index2 = lst.index(0, index1+1)
            return lst[index2+1:].count(7) > 0
        else:
            return False
    else:
        return False


print(check_007([1, 0, 2, 30, 33, 0, 7, 0, 35, 7]))
