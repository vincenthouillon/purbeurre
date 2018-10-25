import json
import random

import mysql.connector
import requests
from colorama import Back, Fore, init

from config import configuration as conf
from config.dbase import Dbase
from purbeurre import header, home

init(autoreset=True)


def display_ls_categories():
    """Displays the categories of the json file
    """
    categories = conf.read_categories()["ls_categories"]

    print("Liste des catégories disponibles :")
    num = 0
    for category in categories:
        num += 1
        print(str(num).center(2, " "), "-", category)

    print("-" * 80)
    category_input = input(
        "Veuillez saisir un nombre entre 1 et {} ou 'q' pour quitter : ".format(len(categories)))

    if category_input.lower() == "q":
        print("\nAu revoir et à bientôt")
        exit()

    else:
        try:
            category_input = int(category_input)
        except:
            error = (
                " Veuillez saisir un nombre entre 1 et {} ou 'q' pour quitter".format(len(categories)))
            header(error)
            display_ls_categories()
        else:
            if category_input > 0 and category_input <= len(categories):
                category = categories[category_input-1]
                print("\nVous avez choisi la catégorie :", category)
                print("-" * 80)
                header()
                display_ls_products(category)

            else:
                error = (
                    "Veuillez saisir un nombre entre 1 et {} ou 'q' pour quitter".format(len(categories)))
                header(error)
                display_ls_categories()


def display_ls_products(category, page_number=1):
    """Display the list of products

    Arguments:
        category {str} -- Category

    Keyword Arguments:
        page_number {int} -- Page number (default: {1})
    """
    url = conf.url_categories(category, page_number)
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


def display_product(code, category):
    """Displays the 'product sheet'

    Arguments:
        code {str} -- Code product
        category {str} -- Category
    """
    category = category
    url = conf.url_product(code)
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


def display_alter_product(code, category):
    """Search alternative product

    Arguments:
        code {str} -- Code product
        category {str} -- Category
    """
    category = category
    url = conf.url_product(code)
    r = requests.get(url).json()
    page_product = json.dumps(r)
    product = json.loads(page_product)
    print("*" * 80)
    # print(product['product']['generic_name_fr'])
    # print(len(product['product']['generic_name_fr']))

    if len(product['product']['generic_name_fr']) == 0:
        keyword = conf.cleaner(product['product']['product_name_fr'])
        print("Produit de subsitution pour :", keyword)
    else:
        keyword = conf.cleaner(product['product']['generic_name_fr'])
        print("Produit de sublistution pour :", keyword)

    if product['product']['nutrition_grades'] != "a":
        url = conf.url_alt_product(keyword)
        r = requests.get(url).json()
        page_alter = json.dumps(r)
        alter = json.loads(page_alter)
        if alter["count"] > 0:
            print("Nombre de produits trouvés en nutriscore 'a':",
                  alter["count"])
            if alter["count"] > 20:
                hazard = random.randint(0, 20)
                # print("URL:", alter["products"][hazard]["url"])
                code = (alter["products"][hazard-1]["code"])
                display_product(code, category)
            else:
                hazard = random.randint(0, alter["count"])
                # print("URL:", alter["products"][hazard]["url"])
                code = (alter["products"][hazard-1]["code"])
                display_product(code, category)
        else:
            url = conf.url_alt_product(keyword, 'b')
            r = requests.get(url).json()
            page_alter = json.dumps(r)
            alter = json.loads(page_alter)
            if alter["count"] > 0:
                print("Nombre de produits trouvés en nutriscore 'b':",
                      alter["count"])
                if alter["count"] > 20:
                    hazard = random.randint(0, 20)
                    # print("URL:", alter["products"][hazard]["url"])
                    code = (alter["products"][hazard-1]["code"])
                    display_product(code, category)
                else:
                    hazard = random.randint(0, alter["count"])
                    # print("URL:", alter["products"][hazard]["url"])
                    code = (alter["products"][hazard-1]["code"])
                    display_product(code, category)
            else:
                url = conf.url_alt_product(keyword, 'c')
                r = requests.get(url).json()
                page_alter = json.dumps(r)
                alter = json.loads(page_alter)
                if alter["count"] > 0:
                    print("Nombre de produits trouvés en nutriscore 'c':",
                          alter["count"])
                    if alter["count"] > 20:
                        hazard = random.randint(0, 20)
                        # print("URL:", alter["products"][hazard]["url"])
                        code = (alter["products"][hazard-1]["code"])
                        display_product(code, category)
                    else:
                        hazard = random.randint(0, alter["count"])
                        # print("URL:", alter["products"][hazard]["url"])
                        code = (alter["products"][hazard-1]["code"])
                        display_product(code, category)
                else:
                    print("\nOups ! Pas de produit de substition trouvé :-(")

    else:
        print("")

    print("-" * 80)
    print("<A> - Accueil")
    print("<R> - Retour")
    print("<E> - Enregistrer")
    print("<Q> - Quitter")

    alter_input = input("\nEntrez votre choix : ")

    if alter_input.lower() == "q":
        print("\nAu revoir et à bientôt")
        exit()

    elif alter_input.lower() == "e":
        try:
            Dbase.insert_tbl_categories(code, category)
        except mysql.connector.Error as err:
            if err.errno == 1062:
                msg = ("Produit déjà enregistré")
                header(msg)
                display_ls_products(category)
        else:
            msg = ("Produit enregistré")
            header(msg)
            display_ls_products(category)

    elif alter_input.lower() == "a":
        header()
        home()

    elif alter_input.lower() == "r":
        header()
        display_ls_products(category)

    else:
        error = ("Saisie incorrecte")
        header(error)
        display_ls_products(category)


def display_all_records():
    """Displays all records in the database
    """
    print("Display all records")
    cnx = Dbase.sql_connect()
    cur = cnx.cursor()
    cur.execute("USE purbeurre")
    cur.execute("""
        SELECT * FROM Records;
    """)
    number_line = 1
    for raw in cur:
        print(f"{raw[0]} - {raw[2]} {raw[3]}")
        number_line += 1

    print("")
    print("-" * 80)
    print("<A> - Accueil")
    print("<Q> - Quitter")
    ask = input(">> ")

    if ask.lower() == "q":
        print("\nAu revoir et à bientôt")
        exit()

    elif ask.lower() == "a":
        header()
        home()

    try:
        ask = int(ask)
    except:
        error = ("Entrée incorrecte")
        header(error)
        display_all_records()
    else:
        header()
        display_record(ask, raw[1], raw[8])


def display_record(ask, code, category):
    """Displays a product registered in the database

    Arguments:
        ask {str} -- User response
        code {str} -- Code product
        category {str} -- Category
    """
    cnx = Dbase.sql_connect()
    cur = cnx.cursor()
    cur.execute("USE purbeurre")

    cur.execute("""
        SELECT * FROM Records WHERE id={}
    """.format(ask))
    product = (cur.fetchone())

    display_product(product[1], product[8])

    print("")
    print("-" * 80)
    print("<A> - Accueil")
    print("<Q> - Quitter")
    print("<R> - Retour")

    ask2 = input(">> ")

    if ask2.lower() == "q":
        print("\nAu revoir et à bientôt")
        exit()

    elif ask2.lower() == "a":
        header()
        home()

    elif ask2.lower() == "r":
        header()
        display_all_records()

    else:
        error = ("Entrée incorrecte")
        header(error)
        # display_all_records()
        display_record(ask, product[1], product[8])
