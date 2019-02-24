# write a function that returns the number of prime numbers that exist up to and including a given number

# 100 --> 25
# 0 and 1 are not prime


def count_prime(num):
    count = 0
    for i in range(2, num+1):
        for j in range(2, i//2+2):
            if j != i and i % j == 0:
                break
        else:
            #            print(i)
            count += 1
    return count


print(count_prime(10))
