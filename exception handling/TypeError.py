'''
 for i in ['a', 'b', 'c']:

    print(i**2)

Traceback (most recent call last):
  File "c:\CODE\python\exception handling\TypeError.py", line 3, in <module>
    print(i**2)
TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'int'

'''

try:
    for i in ['a', 'b', 'c']:

        print(i**2)
except TypeError:
    print("Type Error")
