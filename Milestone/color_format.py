from colorama import Fore
from colorama import init
init()


def print_format_table():

    d = [" ", " "]
    d[0] = Fore.RED + "red"
    d[1] = Fore.GREEN + "green"

    print("TEST {} {}".format(*d))


print_format_table()
