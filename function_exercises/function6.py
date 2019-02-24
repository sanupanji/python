# given an integer n, return true if n is within 10 of either 100 or 200


def within_10_of_100_200(n):
    # return 190 <= n <= 210 or 90 <= n <= 110
    # using abs
    return abs(100 - n) <= 10 or abs(200-n) <= 10


print(within_10_of_100_200(116))
