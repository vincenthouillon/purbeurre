import json
import random

import mysql.connector
import requests

from lib.configuration import cleaner, url_alt_product, url_product
from lib.dbase import Dbase
from menu import displayproduct as dp
from menu import displayproductslist as dpl
from purbeurre import header, home


def display_alter_product(code, category):
    """Search alternative product
    
    Arguments:
        code {str} -- Code product
        category {str} -- Category
    """
    category = category
    url = url_product(code)
    r = requests.get(url).json()
    page_product = json.dumps(r)
    product = json.loads(page_product)
    print("*" * 80)
    # print(product['product']['generic_name_fr'])
    # print(len(product['product']['generic_name_fr']))

    if len(product['product']['generic_name_fr']) == 0:
        keyword = cleaner(product['product']['product_name_fr'])
        print("Produit de subsitution pour :", keyword)
    else:
        keyword = cleaner(product['product']['generic_name_fr'])
        print("Produit de sublistution pour :", keyword)

    if product['product']['nutrition_grades'] != "a":
        url = url_alt_product(keyword)
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
                dp.display_product(code, category)
            else:
                hazard = random.randint(0, alter["count"])
                # print("URL:", alter["products"][hazard]["url"])
                code = (alter["products"][hazard-1]["code"])
                dp.display_product(code, category)
        else:
            url = url_alt_product(keyword, 'b')
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
                    dp.display_product(code, category)
                else:
                    hazard = random.randint(0, alter["count"])
                    # print("URL:", alter["products"][hazard]["url"])
                    code = (alter["products"][hazard-1]["code"])
                    dp.display_product(code, category)
            else:
                url = url_alt_product(keyword, 'c')
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
                        dp.display_product(code, category)
                    else:
                        hazard = random.randint(0, alter["count"])
                        # print("URL:", alter["products"][hazard]["url"])
                        code = (alter["products"][hazard-1]["code"])
                        dp.display_product(code, category)
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
                error = ("Produit déjà enregistré")
                header(error)
                dpl.display_ls_products(category)
        else:
            error = ("Produit enregistré")
            header(error)
            dpl.display_ls_products(category)

    elif alter_input.lower() == "a":
        header()
        home()

    elif alter_input.lower() == "r":
        header()
        dpl.display_ls_products(category)

    else:
        error = ("Saisie incorrecte")
        header(error)
        dpl.display_ls_products(category)
