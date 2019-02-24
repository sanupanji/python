# given a list of integers, return ture if the array contains a 3 next to a 3 somewhere


def consec(lst):
    for i in range(0, len(lst)-1):
        if lst[i] == 3 and lst[i+1] == 3:
            return True
    else:
        return False


print(consec([1, 2, 3, 3, 4, 4, 5]))
