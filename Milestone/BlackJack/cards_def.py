import random

class cards_def():

    dimond = '♦'
    heart = '♥'
    club = '♣'
    spade = '♠'

    ty=(dimond,heart,club,spade)
        
    values = {
            "One":1,
            "Two":2,
            "Three":3,
            "Four":4,
            "Five":5,
            "Six":6,
            "Seven":7,
            "Eight":8,
            "Nine":9,
            "Ten":10,
            "Jack":10,
            "Queen":10,
            "King":10
            }

    #data = { k:list(locals()[ty]) for k in values }
    print(ty)
        

        
    def details():
            return {k:list(ty) for k in values }
            
                    
    def choose():
            
            x = random.choice(list(values.keys()))
            y = random.choice(data[x])
            
            print (f"{x} of {y}")
            data[x].remove(y)



           
        

