'''
Write a Python program which accepts the user's first and last name and print them in reverse order with a space between them. Go to the editor

Sanu Panji --> Panji Sanu
'''

def string_reverse(st):
  
    return ' '.join(reversed(st.split()))


print(string_reverse(input("Enter the full name : ")))

