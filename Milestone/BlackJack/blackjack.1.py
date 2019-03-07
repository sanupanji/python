from Player import Plyer
money = 1000

def start(x):

    p = Plyer()
    print("Player")
    
    Hit = True
    bat = int(input(f"How much money for current deal? You have {x} amount in hand: "))
    
    if (x - bat) > 0:
            
            lscard = []
            
            while Hit == True:
                ls = p.profile()
                lscard.append(ls[1])
                
                while sum(lscard) > 21:
                    if lscard.count(11) == 0:
                        print("BUST")
                        x -= bat
                        p.rerun()
                        start(x)
                    else:
                        lscard = checkA(lscard)

                checksum = sum(lscard)
                        
                        
                    
                print(f"Sum : {checksum}")
                hitstand = input("Do you want to Hit again or Stand, enter HIT or STAND: ").upper()
                if hitstand == "STAND":
                    Hit = False

    else:
        print("you are out of money, want to start again?")
        ch = input("YES or NO? : ").upper()
        if ch == "YES":
            start(money)
        else:
            exit(0) 



def checkA(ls):

    ls[ls.index(11)] =1
    return ls

        
        
        
    
    




print("Computer dealer")


if __name__ == "__main__":
    start(money)
