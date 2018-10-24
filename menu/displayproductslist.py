import json

import requests

from lib.configuration import url_categories
from menu.displayproduct import display_product
from menu.displayalternativeproduct import display_alter_product
from purbeurre import header, home


def display_ls_products(category, page_number=1):

    url = url_categories(category, page_number)
    r = requests.get(url).json()
    products = json.dumps(r)
    page = json.loads(products)
    num_page = page['page']
    total_products = page["count"]
    number_page = int(page["count"]/20 + 1)
    print("Nb de '{}' trouvé(e)s = {} - Page = {} sur {}".format(category,
                                                                 total_products, num_page, number_page))
    product_num = 1
    for x in page['products']:
        print("{:2d} - {}, {}".format(product_num,
                                      x['product_name_fr'], x['quantity']))
        product_num += 1
    print("-" * 80)
    if num_page > 1:
        print("<P ou p> - Page précèdente")
    else:
        print("-")
    print("<S> - Page suivante")
    print("<A> - Accueil")
    print("<Q> - Quitter")

    product_choice = input("\nEntrez votre choix : ")

    if product_choice == "p":
        if num_page > 1:
            header()
            display_ls_products(category, page_number - 1)
        else:
            header()
            display_ls_products(category, page_number=1)

    elif product_choice == "s":
        header()
        display_ls_products(category, page_number + 1)

    elif product_choice == "a":
        header()
        home()

    elif product_choice == "q":
        print("\nAu revoir et à bientôt")
        exit()

    try:
        product_choice = int(product_choice)
    except:
        error = (
            "Veuillez saisir un nombre entre 1 et {}, 'n', 'q'".format(len(page['products'])))
        header(error)
        display_ls_products(category)
    else:
        if product_choice > 0 and product_choice <= len(page['products']):
            code = (page['products'][product_choice-1]['code'])
            header()
            display_product(code, category)
            display_alter_product(code, category)

        else:
            error = (
                " Veuillez saisir un nombre entre 1 et {}, 'n', 'q'".format(len(page['products'])))
            header(error)
            display_ls_products(category, page_number)
