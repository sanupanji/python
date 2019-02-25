import random
import sys
import os
print ("hello")
name = "Sanu"
print("1 + 2 - 3 * 2 =", 1 + 2 - 3 * 2)
print("(1 + 2 - 3) * 2 =", (1 + 2 - 3) * 2)


quote = "\"Always remember your unique,"
 
# A multi-line quote
multi_line_quote = ''' just
like everyone else" '''
 
print(quote + multi_line_quote)
 
# To embed a string in output use %s
print("%d %s %s" % (6, quote, multi_line_quote))

grocery_list = [quote, 'Tomatoes', 'Potatoes', 'Bananas']
print('The first item is', grocery_list[0])
 
# You can change the value stored in a list box
grocery_list[0] = "Green Juice"
