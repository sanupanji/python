# given an integer n, return true if n is within 10 of either 100 or 200


def within_10_of_100_200(n):
    if 190 <= n <= 210 or 90 <= n <= 110:
        return True
    else:
        return False


print(within_10_of_100_200(110))
