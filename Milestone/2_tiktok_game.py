from colorama import Style
from colorama import Fore
from colorama import init
init()
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


LST = ["X", " ", " ", " ", " ", " ", " ", " ", " ", " "]

# .format(dic["1"], dic["2"], dic["3"], dic["4"], dic["5"], dic["6"], dic["7"], dic["8"], dic["9"]))


def print_last(dic, pos=0):

    if pos != 0:
        for i in str(pos):
            dic[int(i)] = Fore.RED + dic[int(i)] + Style.RESET_ALL

    print('''
            |     |
          {} |  {}  |  {}
        ---------------
            |     |
          {} |  {}  |  {}
        ---------------
            |     |
          {} |  {}  |  {}
    '''.format(*dic[1:]))


def print_gui(dic, xo, PLAYER):

    print_last(dic)
    enter_x_o(dic, xo, PLAYER)


def enter_x_o(dic, xo, PLAYER):

    pos = int(input(f"{PLAYER[xo]}, enter {xo} in the position: "))
    if 1 <= pos <= 9:
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

    if dic[1] == dic[2] == dic[3] == "X" or dic[1] == dic[2] == dic[3] == "O":
        check(dic, dic[1], PLAYER, 123)
    elif dic[4] == dic[5] == dic[6] == "X" or dic[4] == dic[5] == dic[6] == "O":
        check(dic, dic[4], PLAYER, 456)
    elif dic[7] == dic[8] == dic[9] == "X" or dic[7] == dic[8] == dic[9] == "O":
        check(dic, dic[7], PLAYER, 789)
    elif dic[1] == dic[4] == dic[7] == "X" or dic[1] == dic[4] == dic[7] == "O":
        check(dic, dic[1], PLAYER, 147)
    elif dic[2] == dic[5] == dic[8] == "X" or dic[2] == dic[5] == dic[8] == "O":
        check(dic, dic[2], PLAYER, 258)
    elif dic[3] == dic[6] == dic[9] == "X" or dic[3] == dic[6] == dic[9] == "O":
        check(dic, dic[3], PLAYER, 369)
    elif dic[1] == dic[5] == dic[9] == "X" or dic[1] == dic[5] == dic[9] == "O":
        check(dic, dic[1], PLAYER, 159)
    elif dic[3] == dic[5] == dic[7] == "X" or dic[3] == dic[5] == dic[7] == "O":
        check(dic, dic[3], PLAYER, 357)

    elif sorted(list(set(dic))) == ["O", "X"]:
        check(dic, xo, PLAYER)

    else:
        if xo == "X":
            print_gui(dic, "O", PLAYER)
        print_gui(dic, "X", PLAYER)


def check(dic, st, PLAYER, draw=0):

    if draw == 0:
        print("Match drawn")
    else:
        print("{} wins".format(PLAYER[st]))
    print_last(dic, draw)
    start = input("Do you want to start again? yes or no : ")
    if start.lower() == "yes":
        for x in range(1, len(dic)):
            dic[x] = " "
        choose(dic)
    quit()


def choose(dic):
    xo = input("PLAYER1, DO YOU WANT TO BE 'X' OR 'O'? ").upper()
    ixo = "O" if xo == "X" else "X"
    PLAYER = {xo: "PLAYER1",  ixo: "PLAYER2"}
    print_gui(dic, xo, PLAYER)


print(choose(LST))
