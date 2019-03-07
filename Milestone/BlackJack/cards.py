import random


class cards():

    dimond = '♦'
    heart = '♥'
    club = '♣'
    spade = '♠'

    ty = [dimond, heart, club, spade]

    values = {
        "One": 11,
        "Two": 2,
        "Three": 3,
        "Four": 4,
        "Five": 5,
        "Six": 6,
        "Seven": 7,
        "Eight": 8,
        "Nine": 9,
        "Ten": 10,
        "Jack": 10,
        "Queen": 10,
        "King": 10
    }

    data = {}
    for key in values:
        data[key] = list(ty)

    def __init__(self):
        del self

    def __str__(self):

        return f"Card types {cards.ty}\nvalues {cards.values}"

    def details(self):
        return cards.data

    def reload(self):
        for key in cards.values:
            cards.data[key] = list(cards.ty)

    def choose(self):

        x = random.choice(list(cards.data.keys()))
        y = random.choice(cards.data[x])
        val = cards.values[x]

        cards.data[x].remove(y)
        if len(cards.data[x]) == 0:

            del cards.data[x]

        return [x, y, val]
