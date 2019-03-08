import time

from Player import Plyer
money = 1000

hidden = """
     ______
    |      |
    |      |
    |HIDDEN|
    |      |
    |______|
      """


def start(inhandmoney):
    
    # global hidden
    p = Plyer()
    if p.count() < 30:
        print("Reshuffling... ") 
        p.reload()
        time.sleep(3)
        
    print(f"Remaining cards {p.count()} ")

    Hit = True
    dealmoney = int(
        input(f"How much money for current deal? You have {inhandmoney} amount in hand: "))

    if (inhandmoney - dealmoney) >= 0:

        lscardman = []
        lscardcomp = []
        lscomp1 = p.profile()
        compvalues = [lscomp1[1]]
        lscardcomp.extend([lscomp1[2][0], hidden])

        lsman1 = p.profile()
        lsman2 = p.profile()
        lines = lsman2[2]
        lscardman.extend([lsman1[1], lsman2[1]])

        plyerman(lscardman, Hit, p, inhandmoney, dealmoney, lines[1:],
                 lscardcomp, compvalues)

    else:
        print("you are out of money, want to start again?")
        ch = input("YES or NO? : ").upper()
        if ch == "YES":
            start(money)
        else:
            exit(0)


def plyerman(lscard, Hit, p, inhandmoney, dealmoney, linesplayer, hiddenls, lscompvalue):

    printcards(linesplayer)
    print(f"Sum : {sum(lscard)}")
    printcards(hiddenls)
    print(f"Sum : {sum(lscompvalue)}")
    hitstand = input(
        "Do you want to Hit again or Stand, enter HIT or STAND: ").upper()
    if hitstand == "STAND":
        Hit = False
        computerprint([hiddenls[0]], lscompvalue,
                      linesplayer, lscard, inhandmoney, dealmoney, p)

    while Hit == True:

        ls = p.profile()
        lscard.append(ls[1])
        printcards(ls[2][1:])
        

        while sum(lscard) > 21:
            if lscard.count(11) == 0:
                print(f"Sum : {sum(lscard)}")
                printcards(hiddenls)
                print(f"Sum : {sum(lscompvalue)}")
                print("BUST")
                inhandmoney -= dealmoney
                p.rerun()
                start(inhandmoney)
            else:
                lscard = checkA(lscard)

        print(f"Sum : {sum(lscard)}")
        printcards(hiddenls)
        print(f"Sum : {sum(lscompvalue)}")

        checksum = sum(lscard)

        hitstand = input(
            "Do you want to Hit again or Stand, enter HIT or STAND: ").upper()
        if hitstand == "STAND":
            Hit = False
            computerprint([hiddenls[0]], lscompvalue, ls[2]
                          [1:len(lscard)+1], lscard, inhandmoney, dealmoney, p)





def computerprint(compcardlist, compvalue, playerls, lsplyercard, inhand, betting, p):
    
  
    compturn = True
    while compturn == True:
        printcards(playerls)
        print(f"Sum : {sum(lsplyercard)}")
        ls = p.profile()
        compvalue.append(ls[1])
        printcards([ls[2][0]]+ls[2][len(lsplyercard)+1:])
        time.sleep(1)
        
        

        while sum(compvalue) > 21:
            if compvalue.count(11) != 0:
                compvalue = checkA(compvalue)
            break
        print(f"Sum : {sum(compvalue)}")
        if sum(compvalue) < sum(lsplyercard):
            continue
        if sum(compvalue) < sum(lsplyercard):
            continue
        elif sum(compvalue) == sum(lsplyercard):
            print("PUSH")
            p.rerun()
            start(inhand)
        elif sum(lsplyercard) < sum(compvalue) <= 21:
            print("Computer wins")
            inhand -= betting
            p.rerun()
            start(inhand)
            compturn = False


        print("BUST")
        print("Player wins")
        inhand += betting
        p.rerun()
        start(inhand)


    
            
def checkA(ls):

    ls[ls.index(11)] = 1
    return ls


def printcards(cardls):

    player = [x for x in range(len(cardls))]
    lines = [cardls[i].splitlines() for i in player]
    #print("=================================================================================")
    for l in zip(*lines):
        print(*l, sep='')

print("Computer dealer")


if __name__ == "__main__":
    start(money)
