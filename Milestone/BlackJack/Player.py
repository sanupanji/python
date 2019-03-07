from cards import cards


class Plyer():

    card = """
     ______ 
    |      |
    |{: ^6}|
    |  of  |
    |{: ^6}|
    |______|
      
      """

    cardls = []
    c = cards()

    def __init__(self):

        del self

    def profile(self, res=0):

        ls = Plyer.c.choose()

        #Plyer.cardls = [Plyer.card.format(ls[0],ls[1]),Plyer.card.format(ls2[0],ls2[1])]
        Plyer.cardls.append(Plyer.card.format(ls[0], ls[1]))
        #player = [x for x in range(len(Plyer.cardls))]
        #lines = [Plyer.cardls[i].splitlines() for i in player]

        return [ls[0], ls[2], Plyer.cardls]

    def details(self):

        print(Plyer.c.details())

    def rerun(self):
        Plyer.cardls = []
