'''
Write a Python program to find whether a given number (accept from the user) is even or odd,
print out an appropriate message to the user. 
'''

def even_odd_check(n):

    if n %2 ==0:
        return "you entered an even number"
    return "you entered an odd number"

print(even_odd_check(int(input("Enter the number : "))))
