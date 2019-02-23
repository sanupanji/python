# given three integers between 1 and 11, if their sum is less then or equal
# to 21, return their sum. if their sum exceeds 21 and there's an eleven, reduce the total sum by 10, finally, if the sum (even after adjustment)exceeds 21, return "BUST"

#  5,6,7 --> 18
# 9,9,9 --> 'BUST'
# 9,9,11 --> 19 (one of the number is 11, so sum - 10)


def sumcheck(*args):
    if sum(args) <= 21:
        return sum(args)
    elif 11 in args and sum(args)-10 <= 21:
        return sum(args)-10
    return "BUST"


print(sumcheck(9, 9, 1))
