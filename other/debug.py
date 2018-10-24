generic_name = "Grains de riz "

categorie = ['Aliments et boissons à base de végétaux', "Aliments d'origine végétale", 'Petit-déjeuners', 'Céréales et pommes de terre', 'Céréales et dérivés', 'Céréales pour petit-déjeuner', 'Riz soufflé', 'Céréales au chocolat']


def cleaner(name):
    exclude = ("de", "des", "au", "aux", 'en', "le", "la", "les", "et", "un", "une")

    produit = name.lower()
    produit = produit.split(" ")
    print(produit)

    for e in exclude:
        for x in produit:
            if x in e:
                print(e)
                produit.remove(e)

    keyword = (" ".join(produit[0:4]))
    return keyword

print(cleaner("Céréales 95% de blé complet"))