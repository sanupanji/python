st = "Print only the swords that starts with s in this sentence"
print(st.split(" "))
for word in st.split(" "):
    if word[0].lower() == "s":  # or word[0] == "S":
        print(word, end=" ")


sw = [x for x in st.split(" ") if x[0] == "s"]
print(sw)
