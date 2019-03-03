
def trycatch():
    try:
        x = int(input("Enter a number: "))
    except ValueError:
        print("Sorry, not an Integer, retry!!")
        trycatch()
    else:
        print(f"you entered {x} as Integer")


trycatch()
