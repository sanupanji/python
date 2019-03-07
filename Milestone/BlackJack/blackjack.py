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


def start(x):

    # global hidden
    p = Plyer()
    print("Player")

    Hit = True
    bat = int(
        input(f"How much money for current deal? You have {x} amount in hand: "))

    if (x - bat) > 0:

        lscardman = []
        lscardcomp = []
        lscomp1 = p.profile()
        compvalues = [lscomp1[1]]
        lscardcomp.extend([lscomp1[2][0], hidden])

        lsman1 = p.profile()
        lsman2 = p.profile()
        lines = lsman2[2]
        lscardman.extend([lsman1[1], lsman2[1]])

        plyerman(lscardman, Hit, p, x, bat, lines[1:],
                 lscardcomp, compvalues)

    else:
        print("you are out of money, want to start again?")
        ch = input("YES or NO? : ").upper()
        if ch == "YES":
            start(money)
        else:
            exit(0)


def plyerman(lscard, Hit, p, x, bat, linesplayer, hiddenls, lscompvalue):

    printcards(linesplayer)
    print(f"Sum : {sum(lscard)}")
    printcards(hiddenls)
    print(f"Sum : {sum(lscompvalue)}")
    hitstand = input(
        "Do you want to Hit again or Stand, enter HIT or STAND: ").upper()
    if hitstand == "STAND":
        Hit = False
        computerprint([hiddenls[0]], lscompvalue,
                      linesplayer, lscard, x, bat, p)

    while Hit == True:

        ls = p.profile()
        lscard.append(ls[1])
        printcards(ls[2][1:])

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
        printcards(hiddenls)
        print(f"Sum : {sum(lscompvalue)}")
        hitstand = input(
            "Do you want to Hit again or Stand, enter HIT or STAND: ").upper()
        if hitstand == "STAND":
            Hit = False
            computerprint([hiddenls[0]], lscompvalue, ls[2]
                          [1:len(lscard)+1], lscard, x, bat, p)


def checkA(ls):

    ls[ls.index(11)] = 1
    return ls


def printcards(cardls):

    player = [x for x in range(len(cardls))]
    lines = [cardls[i].splitlines() for i in player]

    for l in zip(*lines):
        print(*l, sep='')


def computerprint(lscomp, compvalue, playerls, lsplyercard, inhand, betting, p):
    ls = p.profile()
    compvalue.append(ls[1])
    printcards([ls[2][0]]+ls[2][len(lsplyercard):])
    print(f"Sum : {sum(compvalue)}")
    printcards(playerls)
    print(f"Sum : {sum(lsplyercard)}")
    compturn = True
    while compturn == True:

        if sum(compvalue) < sum(lsplyercard):
            printcards(lscomp)
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

        elif sum(compvalue) > 21:

            while compvalue.count(11) != 0:
                compvalue = checkA(compvalue)

                print("BUST")
                inhand -= betting
                p.rerun()
                start(inhand)
            else:
                compvalue = checkA(compvalue)


print("Computer dealer")


if __name__ == "__main__":
    start(money)
