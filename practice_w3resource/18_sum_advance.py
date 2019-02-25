'''
Write a Python program to calculate the sum of three given numbers,
if the values are equal then return thrice of their sum.'''

def sum_advance(*args):

    if len(set(args)) == 1:
        return sum(args)*3

    return sum(args)


print(sum_advance(4,3,3))

    
