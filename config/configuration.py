import json


def read_categories():
    """Read json file and return a list of categories
    """
    with open("./config/main_categories.json", encoding="utf-8") as f:
        json_categories = json.load(f)
        return json_categories


def url_categories(category, page=1):
    """Return the url of the categories page
    
    Arguments:
        category {str} -- Category
    
    Keyword Arguments:
        page {int} -- Page number (default: {1})
    """
    url = ("https://fr.openfoodfacts.org/cgi/search.pl?action=process&tagtype_0=categories&tag_contains_0=contains&tag_0={}&sort_by=unique_scans_n&page_size=20&axis_x=energy&axis_y=products_n&action=display&page={}&json=1").format(
        category, page)
    return url


def url_product(code):
    """Return the url of a product page
    
    Arguments:
        code {str} -- Code product
    """
    url = ("https://fr.openfoodfacts.org/api/v0/produit/{}.json").format(code)
    return url


def url_alt_product(keyword, nutriscore="a"):
    """Return the url for alternative products
    
    Arguments:
        keyword {str} -- Keyword for a research
    
    Keyword Arguments:
        nutriscore {str} -- Nutriscore (default: {"a"})
    """
    url = ("https://fr.openfoodfacts.org/cgi/search.pl?action=process&search_terms={}&tagtype_0=nutrition_grades&tag_contains_0=contains&tag_0={}&sort_by=unique_scans_n&page_size=20&axis_x=energy&axis_y=products_n&action=display&json=1").format(keyword, nutriscore)
    return url

def cleaner(name):
    """Delete articles in product names
    
    Arguments:
        name {str} -- Name or generic name of product
    """
    exclude = ("de", "des", "au", "aux", 'en', "le", "la", "les", "et", "un", "une", "du", "à")

    produit = name.lower()
    produit = produit.split(" ")

    for e in exclude:
        for x in produit:
            if x in e:
                try:
                    produit.remove(e)
                except:
                    return x

    keyword = (" ".join(produit[0:5]))
    return keyword


def main():
    read_categories()


if __name__ == '__main__':
    main()
