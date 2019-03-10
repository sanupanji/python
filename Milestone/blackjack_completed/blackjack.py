import time

from Player import Plyer
money = 1000
p = Plyer()
Hit = True
hidden = """
     ______
    |      |
    |      |
    |HIDDEN|
    |      |
    |      |
     ‾‾‾‾‾‾
      """


def start(inhandmoney):

    global p

    if p.count() < 30:
        print("Reshuffling... ")
        p.reload()
        time.sleep(3)

    print(f"Remaining cards {p.count()} ")

    dealmoney = int(
        input(f"How much money for current deal? You have {inhandmoney} amount in hand: "))

    if (inhandmoney - dealmoney) >= 0:

        compchoose = p.profile()
        compcardvalue = [compchoose[1]]
        compcardlist = [compchoose[2][0], hidden]

        playerchoose1 = p.profile()
        playerchoose2 = p.profile()

        # as first card from list belongs to computer
        playercardlist = playerchoose2[2][1:]
        playercardvalue = [playerchoose1[1], playerchoose2[1]]

        plyerman(compcardlist, compcardvalue, playercardlist,
                 playercardvalue, inhandmoney, dealmoney)

    else:
        print("you are out of money, want to start again?")
        ch = input("YES or NO? : ").upper()
        if ch == "YES":
            start(money)
        else:
            exit(0)


def plyerman(compcardlist, compcardvalue, playercardlist, playercardvalue, inhandmoney, dealmoney):

    global p
    print("\n"*100)
    printcards(playercardlist)
    print(f"Sum : {sum(playercardvalue)}")
    printcards(compcardlist)
    print(f"Sum : {sum(compcardvalue)}")
    if sum(playercardvalue) >= 21:
        print("Jackpot, Player wins")
        inhandmoney += dealmoney
        p.rerun()
        start(inhandmoney)

    hitstand = input(
        "Do you want to Hit again or Stand, enter HIT or STAND: ").upper()
    if hitstand == " ":
        computerprint([compcardlist[0]], compcardvalue,
                      playercardlist, playercardvalue, inhandmoney, dealmoney)

    while True:

        playerchoose = p.profile()
        playercardvalue.append(playerchoose[1])
        print("\n"*100)
        printcards(playerchoose[2][1:])

        while sum(playercardvalue) > 21:
            if playercardvalue.count(11) == 0:
                print(f"Sum : {sum(playercardvalue)}")
                printcards(compcardlist)
                print(f"Sum : {sum(compcardvalue)}")
                print("BUST, Player loose")
                inhandmoney -= dealmoney
                p.rerun()
                start(inhandmoney)
            else:
                playercardvalue = checkA(playercardvalue)

        print(f"Sum : {sum(playercardvalue)}")
        printcards(compcardlist)
        print(f"Sum : {sum(compcardvalue)}")

        hitstand = input(
            "Do you want to Hit again or Stand, enter HIT or STAND: ").upper()
        if hitstand == " ":
            computerprint([compcardlist[0]], compcardvalue, playerchoose[2][1:len(
                playercardvalue)+1], playercardvalue, inhandmoney, dealmoney)


def computerprint(compcardlist, compcardvalue, playercardlist, playercardvalue, inhandmoney, dealmoney):

    while True:

        print("\n"*100)
        printcards(playercardlist)
        print(f"Sum : {sum(playercardvalue)}")
        compchoose = p.profile()
        compcardvalue.append(compchoose[1])
        printcards([compchoose[2][0]]+compchoose[2][len(playercardvalue)+1:])
        time.sleep(1.5)
        while sum(compcardvalue) > 21:
            if compcardvalue.count(11) != 0:
                compcardvalue = checkA(compcardvalue)
            break
        print(f"Sum : {sum(compcardvalue)}")
        time.sleep(1.5)
        if sum(compcardvalue) < sum(playercardvalue):
            continue

        elif sum(compcardvalue) == sum(playercardvalue):
            print("WOW!! A tie, PUSH")
            p.rerun()
            start(inhandmoney)
        elif sum(playercardvalue) < sum(compcardvalue) <= 21:
            print("Player BUST, Computer wins")
            inhandmoney -= dealmoney
            p.rerun()
            start(inhandmoney)

        print("BUST, Player Wins")
        inhandmoney += dealmoney
        p.rerun()
        start(inhandmoney)


def checkA(ls):

    ls[ls.index(11)] = 1
    return ls


def printcards(cardls):

    player = [x for x in range(len(cardls))]
    lines = [cardls[i].splitlines() for i in player]
    for l in zip(*lines):
        print(*l, sep='')


if __name__ == "__main__":
    start(money)
