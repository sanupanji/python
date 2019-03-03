str = "Print every word in this sentence that has an even number of letters"

for word in str.split(" "):
    if len(word) % 2 == 0:
        print("even")
    else:
        print(word)


#list conprehension #
print([f"even {word}" for word in str.split(" ") if len(word) % 2 == 0])
