# reverse words in given sentence


def reverse_w(senten):
    revstr = senten.split()
    revstr.reverse()
    return ' '.join(revstr)


print(reverse_w("i am panji sanu"))
