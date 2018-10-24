
from lib.configuration import read_categories
from menu.displayproductslist import display_ls_products
from purbeurre import header, home


def display_ls_categories():
    """Displays the categories of the json file
    """
    categories = read_categories()["ls_categories"]

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
