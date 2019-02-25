'''
Write a Python program to print the calendar of a given month and year.
Note : Use 'calendar' module.
'''
import calendar

def calender_m(y, m):
    
    return calendar.month(y, m)    

print (calender_m(int(input("Enter the year: ")),int(input("Enter the month: "))))

