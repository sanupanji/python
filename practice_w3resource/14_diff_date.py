'''
Write a Python program to calculate number of days between two dates.
Sample dates : (2014, 7, 2), (2014, 7, 11)
Expected output : 9 days
'''
from datetime import date

def diff_date(t1,t2):

    return abs(date(t1[0],t1[1],t1[2])- date(t2[0],t2[1],t2[2]))
  


print(diff_date((2019,2,2),(2019,2,3)))
