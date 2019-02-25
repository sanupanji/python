'''
Write a Python program which accepts the radius of a circle from the user and compute the area. Go to the editor
Sample Output : 
r = 1.1
Area = 3.8013271108436504

'''
from math import pi

def area_cir(rad):
    return pi*(rad**2)



print(area_cir(float(input("Enter the radius : "))))
