'''
Write a Python program that will accept the base and height of a triangle
and compute the area
'''

def area_triangle(base,h):

    return f"the are is : {(base*h)/2} unit"


print(area_triangle(float(input("Enter the value of base: ")),float(input("Enter the value of hight: "))))
