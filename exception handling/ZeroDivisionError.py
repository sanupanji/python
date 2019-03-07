'''

z = 5/0
 Traceback (most recent call last):
  File "c:\CODE\python\exception handling\ZeroDivisionError.py", line 1, in <module>
    z = 5/0
ZeroDivisionError: division by zero
'''
try:
    x = int(input("Enter the first number: "))
    y = int(input("Enter the second number: "))

    print(x/y)
except ZeroDivisionError:
    print("Can not divide by '0'")
finally:
    print("All done")
