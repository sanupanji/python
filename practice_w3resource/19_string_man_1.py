'''
Write a Python program to get a new string
from a given string where "Is" has been added to the front.
If the given string already begins with "Is" then return the string unchanged. 
'''

def string_man_1(st):

    if st[:2].lower() == "is":
        return st
    return "Is" + st

print(string_man_1(input("enter the string : ")))
