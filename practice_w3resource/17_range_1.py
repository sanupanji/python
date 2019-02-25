'''
Write a Python program to test whether a number is within 100 of 1000 or 2000.
'''

def range_100(i):

    if abs(2000-i) <=100 or abs(1000-i) <=100:
        return f"{i} is within 100 of 1000 or 2000"
    return f"{i} is not within 100 of 1000 or 2000"

print(range_100(int(input("enter the number: "))))
