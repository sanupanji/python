'''
Write a Python program to get the difference between a given number and 17,
if the number is greater than 17 return double the absolute difference.
'''

def int_man_17(i):

    if i > 17:
        return 2*abs(17-i)
    return 17-i

print(int_man_17(int(input("enter the number: "))))
