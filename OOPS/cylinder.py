'''
fill in the cylinder class methods to accepts hight and radius
and return the surface area and volume of the cylinder

cylinder(3,2)
cylinder(8,10)

c = cylinder(2,4)


surface_area = (2 * pi * radius * hight) + (2 * pi * (r**2)) or 2 * pi * radius * (radius+hight)
volume = pi * hight * (r**2)
'''
from math import pi


class cylinder():

    def __init__(self, radius, hight):

        self.r = radius
        self.h = hight

    def surface_area(self):

        return 2 * pi * self.r * (self.r+self.h)

    def volume(self):

        return pi * self.h * (self.r ** 2)


cy = cylinder(2, 4)
print(cy.volume())
print(cy.surface_area())
