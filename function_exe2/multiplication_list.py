# multiply all the number is list
import math


def multiply_list(lst):

    multi = 1
    for i in lst:
        multi *= i

    return multi


print(multiply_list([1, 4, -2, 8]))
