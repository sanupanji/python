# write a function that returns the lesser of two given numbers if both numbers are even
#  but returns the greater if one or both numbers are odd


def greater(num1, num2):
    if num1 % 2 == 0 and num2 % 2 == 0:
        if num1 < num2:
            return num1
        else:
            return num2
    else:
        if num1 < num2:
            return num2
        else:
            return num1


print(greater(int(input("first number: ")), int(input("second number: "))))

# using min max


def greaterwith(num1, num2):
    if num1 % 2 == 0 and num2 % 2 == 0:
        return min(num1, num2)
    else:
        return max(num1, num2)


print(greaterwith(int(input("first number: ")), int(input("second number: "))))
