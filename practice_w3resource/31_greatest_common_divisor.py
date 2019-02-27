'''Write a Python program to compute the greatest common divisor (GCD)
of two positive integers. '''

'''
from math import gcd

def greatest_common_divisor(n,m):

    return gcd(n,m)

print(greatest_common_divisor(int(input("Enter 1st: ")),int(input("Enter 2nd: "))))

'''

def greatest_common_divisor_without_import(n,m):

    if max(n,m)%min(n,m) == 0:
        return min(n,m)
    else:
        for i in range(min(n,m)//2,0,-1):
            if n%i == 0 and m%i ==0:
                return i
    return 1

print(greatest_common_divisor_without_import(int(input("Enter 1st: ")),int(input("Enter 2nd: "))))



