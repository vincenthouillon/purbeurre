#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import os

from colorama import Back, Fore, init

from lib.configuration import (cleaner, read_categories, url_alt_product,
                               url_categories, url_product)
from menu import displaycategories as dc

init(autoreset=True)


def header(msg_error=""):
    """Displays the program header
    
    Keyword Arguments:
        msg_error {str} -- [description] (default: {""})
    """
    os.system("cls")
    header = " PurBeurre "
    print(Back.YELLOW + (" " * 80))
    print(Back.YELLOW + Fore.BLACK + header.center(80, " "))
    print(Back.YELLOW + (" " * 80))
    if msg_error:
        print(Back.RED + msg_error.center(80, ' ') + "\n" + Back.RESET)
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
        dc.display_ls_categories()
    elif home_input == "2":
        print("\nComing soon!")
        exit()
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
