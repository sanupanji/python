

'''
Write a Python program to test whether a passed letter is a vowel or not
'''

def vowel_check(ch):

    if len(ch) != 1:
        return "wrong input !!!"
    elif ['a','e','i','o','u'].count(ch.lower()) == 1:
        return "Entered charecter is vowel"
    return "Entered charecter is not vowel"
        

print(vowel_check(input("Enter a single alphabet : ")))