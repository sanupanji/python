'''
cards class 
'''


class cards():

    type = ('Hearts', 'Spades', 'Club', 'Diamonds')
    numbers = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
        "ten": 10,
        "jack": 10,
        "queen": 10,
        "king": 10
    }

    def __init__(self):
        pass

    def value(self, type, num):
        return cards.numbers[num]


class deck(cards):

    def __init__(self):
        pass


c = cards()

print(c.numbers["one"])
