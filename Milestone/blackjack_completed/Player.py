from cards import cards


class Plyer(cards):

    card = """
     ______ 
    |{: <6}|
    |      |
    |{: ^6}|
    |      |
    |{: >6}|
     ‾‾‾‾‾‾ 
    """

    cardls = []

    def __init__(self):

        del self

    def profile(self, res=0):

        ls = self.choose()
        Plyer.cardls.append(Plyer.card.format(ls[1], ls[0], ls[1]))

        return [ls[0], ls[2], Plyer.cardls]

    def rerun(self):
        Plyer.cardls = []
