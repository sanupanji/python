# given a list of integers, return ture if the array contains a 3 next to a 3 somewhere


def consec(lst):
    for i in lst:
        if i == 3:
        return lst[lst.index(3)+1] == 3


print(consec([1, 2, 3, 4, 4, 5]))
