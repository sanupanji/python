'''
Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn. Go to the editor
Sample value of n is 5 
Expected Result : 615
'''

def int_as_str(i):

   # return i+11*i+111*i
   return i+int(f"{i}{i}")+int(f"{i}{i}{i}")
   


print(int_as_str(int(input("Enter an integer : "))))
