# given a value , return a value that is twice as far away on the other side of 7
# 4 --> 13
# 10 --> 1


def other_side_of_7(num):
    if num >= 7:
        return 7-(num-7)*2
    else:
        return 7+(7-num)*2


print(other_side_of_7(-1))
