'''
fill in the line class methods to accepts coordintes as a pair of tuples
and return the slope and distance of the line

cor1=(3,2)
cor2=(8,10)

li = line(cor1,cor2)

li.distance()
li.slope()

distance = sqrt((x2-x1)**2 + (y2-y1)**2)
slope = (y2-y1)/(x2-x1)
'''
from math import sqrt


class line():

    def __init__(self, cor1, cor2):
        '''self.x1 = cor1[0]
        self.y1 = cor1[1]
        self.x2 = cor2[0]
        self.y2 = cor2[1]
'''
        self.x1, self.y1 = cor1
        self.x2, self.y2 = cor2

    def distance(self):

        return sqrt((self.x2-self.x1)**2 + (self.y2-self.y1)**2)

    def slope(self):

        return (self.y2-self.y1)/(self.x2-self.x1)


cor1 = (1, 9)
cor2 = (9, 1)


li = line(cor1, cor2)
print(li.distance())
print(li.slope())
