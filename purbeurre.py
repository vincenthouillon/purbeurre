#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import os

from colorama import Back, Fore, init

from config import configuration as conf
from config import display as dis

init(autoreset=True)


def header(msg=""):
    """Displays the program header
    
    Keyword Arguments:
        msg {str} -- Message (default: {""})
    """
    os.system("cls")
    header = " PurBeurre "
    print(Back.YELLOW + (" " * 80))
    print(Back.YELLOW + Fore.BLACK + header.center(80, " "))
    print(Back.YELLOW + (" " * 80))
    if msg:
        print(Back.RED + msg.center(80, ' ') + "\n" + Back.RESET)
    else:
        print("\n")

def home():
    """Display program home
    """
    print("1 - Quel aliment souhaitez-vous remplacer ?")
    print("2 - Retouver mes aliments substitués.")
    print("q - Quitter")
    home_input = input("\nEntrez votre choix : ")

    if home_input == "1":
        header()
        dis.display_ls_categories()

    # :::::::::::::::::::::::::: DISPLAY RECORD ::::::::::::::::::::::::::
    elif home_input == "2":
        header()
        dis.display_all_records()

    elif home_input.lower() == "q":
        print("\nAu revoir et à bientôt...")
        exit()

    else:
        error = ("Veuillez saisir un nombre entre 1 et 2 ou 'q' pour quitter")
        header(error)
        home()


def main():
    header()
    home()

if __name__ == '__main__':
    main()
