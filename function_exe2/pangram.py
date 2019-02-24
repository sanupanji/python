## check pangrm #

# words or sentance that contains every letter atleast once
import string


def pangram(st):

    print(set(st.replace(" ", "").lower()))
    print(set(map(chr, range(97, 123))))
    return set(st.replace(" ", "").lower()) == set(map(chr, range(97, 123)))


print(pangram("a quick brown fox Jumps over the lazy dog"))


# using string module


def pangram_mod(st):

    print(''.join(sorted(list(set(st.replace(" ", "").lower())))))
    print(string.ascii_lowercase)
    return ''.join(sorted(list(set(st.replace(" ", "").lower())))) == string.ascii_lowercase


print(pangram_mod("a quick brown fox Jumps over the lazy dog"))
