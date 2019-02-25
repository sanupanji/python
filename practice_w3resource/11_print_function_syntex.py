'''
Write a Python program to print the documents (syntax, description etc.) of Python built-in function(s). 
Sample function : abs()
Expected Result : 
abs(number) -> number
Return the absolute value of the argument.
'''

def function_syn(fn):
    return eval(fn).__doc__

print(function_syn(input("Enter the function name : ")))
