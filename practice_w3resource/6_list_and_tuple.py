'''Write a Python program which accepts a sequence of comma-separated numbers from user and generate a list and a tuple with those numbers. Go to the editor
Sample data : 3, 5, 7, 23
Output : 
List : ['3', ' 5', ' 7', ' 23'] 
Tuple : ('3', ' 5', ' 7', ' 23')
'''

def list_and_tuple(st):

    return (f"""List : {st.split(',')}
Tuple : {tuple(st.split(','))}""")

print(list_and_tuple(input("Enter a sequence of comma-separated numbers : ")))
