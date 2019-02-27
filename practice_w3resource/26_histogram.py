'''
Write a Python program to create a histogram from
a given list of integers. with char '#'

'''

def histogram(lst):

    h=""
    for i in lst:
        h+="#"*int(i) + "\n"
 
    return h

print(histogram(list(input("Enter numbers: "))))


'''
AI : Print in virtical '''
