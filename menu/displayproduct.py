import json

import requests
from colorama import Back, Fore, init

from lib.configuration import url_product
from menu import displayalternativeproduct as dap

init(autoreset=True)


def display_product(code, category):
    """Displays the 'product sheet'
    
    Arguments:
        code {str} -- Code product
        category {str} -- Category
    """
    category = category
    url = url_product(code)
    r = requests.get(url).json()
    page_product = json.dumps(r)

    product = json.loads(page_product)
    line_1 = "Code produit ...........: "
    line_2 = "Nom du produit .........: "
    line_3 = "Quantité ...............: "
    line_4 = "Fabriquant .............: "
    line_5 = "Suggestion de magasin ..: "
    line_6 = "Nutri-score ............: "
    line_7 = "Page OpenFoodFacts .....: "

    print(f"{line_1}{product['code']}")
    print(f"{line_2}{product['product']['product_name_fr']}")
    print(f"{line_3}{product['product']['quantity']}")
    print(f"{line_4}{product['product']['brands']}")
    print(f"{line_5}{product['product']['stores']}")

    if product['product']['nutrition_grades'] == "a":
        print(line_6 + Back.GREEN + Fore.BLACK + " " +
              product['product']['nutrition_grades'] + " ")
    elif product['product']['nutrition_grades'] == "b":
        print(line_6 + Back.GREEN + Fore.YELLOW + " " +
              product['product']['nutrition_grades'] + " ")
    elif product['product']['nutrition_grades'] == "c":
        print(line_6 + Back.YELLOW + Fore.BLACK + " " +
              product['product']['nutrition_grades'] + " ")
    elif product['product']['nutrition_grades'] == "d":
        print(line_6 + Back.YELLOW + Fore.RED + " " +
              product['product']['nutrition_grades'] + " ")
    elif product['product']['nutrition_grades'] == "e":
        print(line_6 + Back.RED + Fore.BLACK + " " +
              product['product']['nutrition_grades'] + " ")

    print(f"{line_7}https://fr.openfoodfacts.org/produit/\
{product['product']['code']}")

