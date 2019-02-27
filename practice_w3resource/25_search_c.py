'''
Write a Python program to check whether a specified value is contained in a group of values. Go to the editor
Test Data : 
3 -> [1, 5, 8, 3] : True
-1 -> [1, 5, 8, 3] : False
'''

def grep(lst,n):

    return n in lst

ls=[2,43,565,66,453,1,2,3,4,5,6,78,9]
print(grep(ls,int(input("Enter the number to srarch: "))))
    
