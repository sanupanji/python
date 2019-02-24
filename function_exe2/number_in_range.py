# check if a given number is in the given range


def range_check(num, low, high):

    if low <= num <= high:
        return f"{num} is in range between {low} and {high}"
    else:
        return "{} is out of range of {} and {}".format(num, low, high)


print(range_check(3, 4, 7))

## return boolean ##


def range_bool(num, low, high):

    return low <= num <= high


print(range_bool(3, 4, 7))
