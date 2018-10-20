import json
import requests
from colorama import Back, Fore, init

from configuration import read_categories, url_categories

init(autoreset=True)


def header():
    header = " PurBeurre "
    print(Back.YELLOW + (" " * 80))
    print(Back.YELLOW + Fore.BLACK + header.center(80, " "))
    print(Back.YELLOW + (" " * 80))
    print("")


def home():
    print("1 - Quel aliment souhaitez-vous remplacer ?")
    print("2 - Retouver mes aliments substitués.")
    print("3 - Quitter")
    home_input = input("\nEntrez votre choix : ")

    try:
        home_input = int(home_input)
    except:
        print(Back.RED + "\nErreur:" + Back.RESET +
              " Veuillez saisir un nombre entre 1 et 3\n")
    else:
        if home_input == 1:
            display_ls_categories()
        elif home_input == 2:
            print("\nComing soon!")
            exit()
        elif home_input == 3:
            print("\nAu revoir et à bientôt...")
            exit()
        else:
            print(Back.RED + "\nErreur:" + Back.RESET +
                  " Veuillez saisir un nombre entre 1 et 3\n")
            home()


def display_ls_categories():
    categories = read_categories()["ls_categories"]

    print("\nListe des catégories disponibles :")
    num = 0
    for category in categories:
        num += 1
        print(str(num).center(2, " "), "-", category)

    category_input = input("\nEntrez votre choix : ")

    try:
        category_input = int(category_input)
    except:
        print(Back.RED + "\nErreur:" + Back.RESET +
              " Veuillez saisir un nombre entre 1 et {}\n".format(len(categories)))
        display_ls_categories()
    else:
        if category_input > 0 and category_input <= len(categories):
            category = categories[category_input-1]
            print("\nVous avez choisi la catégorie :", category)
            print("-" * 80)

            display_ls_products(category)

        else:
            print(Back.RED + "\nErreur:" + Back.RESET +
                  " Veuillez saisir un nombre entre 1 et {}\n".format(len(categories)))
            display_ls_categories()


def display_ls_products(category, page_number=1):
    url = url_categories(category, page_number)
    r = requests.get(url).json()
    # print(r.headers["content-type"])

    products = json.dumps(r)
    # ! Récupération des numéros de pages
    page = json.loads(products)
    num_page = page['page']
    print("Page = {}".format(num_page))
    product_num = 1
    for x in page['products']:
        print("{:2d} - {}, {}".format(product_num,
                                      x['product_name_fr'], x['quantity']))
        # print(x['generic_name_fr'])
        # print(x['stores'])
        # print(x['nutrition_grades'])
        # print(x['url'])
        # print("-" * 79)
        product_num += 1
    print("-" * 79)
    if num_page > 1:
        print("40 - Previous page")
    else:
        print("")
    print("50 - Next page")
    print("60 - Home page")

    product_choice = input("\nEntrez votre choix : ")

    try:
        product_input = int(product_choice)
    except:
        print(Back.RED + "\nErreur:" + Back.RESET +
              " Veuillez saisir un nombre entre 1 et {}\n".format(len(page['products'])))
        display_ls_categories()
    else:
        if product_input > 0 and product_input <= len(page['products']):
            print("\nVous avez choisi l'aliment :",
                  page['products'][product_input-1]['product_name_fr'])
            print("-" * 80)
            print((page['products'][product_input-1]['url']))
            print((page['products'][product_input-1]['code']))

            # url = (("https://fr.openfoodfacts.org/cgi/search.pl?action=process&tagtype_0=categories&tag_contains_0=contains&tag_0={}&sort_by=unique_scans_n&page_size=20&axis_x=energy&axis_y=products_n&action=display&json=1").format(
            #     page[product_input]))
            # display_ls_products(url)

        elif product_input == 50:
            display_ls_products(category, page_number + 1)
        
        elif product_input == 40:
            if num_page > 1:
                display_ls_products(category, page_number - 1)
            else:
                display_ls_products(category, page_number=1)

        else:
            print(Back.RED + "\nErreur:" + Back.RESET +
                  " Veuillez saisir un nombre entre 1 et {}\n".format(len(page['products'])))
            display_ls_products(category, page_number)


def main(): 
    header()
    home()


if __name__ == '__main__':
    main()
