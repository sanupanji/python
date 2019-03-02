'''
tiktok
functions:
    1. print the gui
            |    |
        1   |2   |3
        ---------------
            |    |
        4   |5   |6
        ---------------
            |    |
        7   |8   |9

     2. print X or O

'''
from colorama import Fore
from colorama import Style


DICMAIN = {"1": " ",  "2": " ",  "3": " ", "4": " ",
           "5": " ", "6": " ", "7": " ", "8": " ", "9": " "}

# .format(dic["1"], dic["2"], dic["3"], dic["4"], dic["5"], dic["6"], dic["7"], dic["8"], dic["9"]))


def print_last(dic):

    print('''
            |     |
          {} |  {}  |  {}
        ---------------
            |     |
          {} |  {}  |  {}
        ---------------
            |     |
          {} |  {}  |  {}
    '''.format(dic["1"], dic["2"], dic["3"], dic["4"], dic["5"], dic["6"], dic["7"], dic["8"], dic["9"]))


def print_gui(dic, xo, PLAYER):

    print_last(dic)
    enter_x_o(dic, xo, PLAYER)


def enter_x_o(dic, xo, PLAYER):

    pos = input(f"{PLAYER[xo]}, enter {xo} in the position: ")
    if 1 <= int(pos) <= 9:
        if dic[pos] != "X" and dic[pos] != "O":
            dic[pos] = xo
        else:
            print(f"position {pos} already taken, retry")
            enter_x_o(dic, xo, PLAYER)
    else:
        print("Only 1 to 9 position available, retry")
        enter_x_o(dic, xo, PLAYER)
    logic(dic, xo, PLAYER)


def logic(dic, xo, PLAYER):

    if dic["1"] == dic["2"] == dic["3"] == "X" or dic["1"] == dic["2"] == dic["3"] == "O":
        check(dic, dic["1"], PLAYER)
    elif dic["4"] == dic["5"] == dic["6"] == "X" or dic["4"] == dic["5"] == dic["6"] == "O":
        check(dic, dic["4"], PLAYER)
    elif dic["7"] == dic["8"] == dic["9"] == "X" or dic["7"] == dic["8"] == dic["9"] == "O":
        check(dic, dic["7"], PLAYER)
    elif dic["1"] == dic["4"] == dic["7"] == "X" or dic["1"] == dic["4"] == dic["7"] == "O":
        check(dic, dic["1"], PLAYER)
    elif dic["2"] == dic["5"] == dic["8"] == "X" or dic["2"] == dic["5"] == dic["8"] == "O":
        check(dic, dic["2"], PLAYER)
    elif dic["3"] == dic["6"] == dic["9"] == "X" or dic["3"] == dic["6"] == dic["9"] == "O":
        check(dic, dic["3"], PLAYER)
    elif dic["1"] == dic["5"] == dic["9"] == "X" or dic["1"] == dic["5"] == dic["9"] == "O":
        check(dic, dic["1"], PLAYER)
    elif dic["3"] == dic["5"] == dic["7"] == "X" or dic["3"] == dic["5"] == dic["7"] == "O":
        check(dic, dic["3"], PLAYER)

    elif sorted(list(set(dic.values()))) == ["O", "X"]:
        check(dic, xo, PLAYER, 1)

    else:
        if xo == "X":
            print_gui(dic, "O", PLAYER)
        print_gui(dic, "X", PLAYER)


def check(dic, st, PLAYER, draw=0):

    if draw == 0:
        print("{} wins".format(PLAYER[st]))
    else:
        print("Match drawn")
    print_last(dic)
    start = input("Do you want to start again? yes or no : ")
    if start.lower() == "yes":
        for x in dic:
            dic[x] = " "
        choose(dic)
    quit()


def choose(dic):
    xo = input("PLAYER1, DO YOU WANT TO BE 'X' OR 'O'? ").upper()
    ixo = "O" if xo == "X" else "X"
    PLAYER = {xo: "PLAYER1",  ixo: "PLAYER2"}
    print_gui(dic, xo, PLAYER)


print(choose(DICMAIN))
