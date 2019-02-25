'''
Write a Python program to accept a filename from the user and print the extension of that. Go to the editor
Sample filename : abc.java 
Output : java
'''

def print_file_extn(file):

    return file[file.rfind('.')+1:]

print(print_file_extn(input("Enter filename with extention : ")))
