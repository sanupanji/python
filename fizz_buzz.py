def fizz_buzz(num):
    if num % 15 == 0:
        return "FizzBuzz"
    elif num % 5 == 0:
        return "buzz"
    elif num % 3 == 0:
        return "fizz"
    else:
        return num


print(fizz_buzz(44))
