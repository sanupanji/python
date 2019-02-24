# given 2 integers return true if the sum of the integers is 20 or if one of the integers is 20, if not return false


def check_20(*args):
    return sum(args) == 20 or 20 in args


print(check_20(113, 20))
