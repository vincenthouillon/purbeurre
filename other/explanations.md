# Projet 05 : Utilisé les données publiques d'OpenFoodFacts

> Vincent Houillon - Formation "Développeur d'application - Python"

* **Code source:** https://github.com/vincenthouillon/purbeurre
* **Tableau agile:** https://github.com/vincenthouillon/purbeurre/projects/1

## Méthodologie

Le programme affiche une liste des catégories principales.
L'utilisateur choisis une catégorie et le programme affiche une liste de 20 produits comme sur le site OpenFoodFacts.
L'utilisateur peut naviguer dans les différentes pages.

Quand on sélectionne un produit, le programme via l'API va récupérer les infos suivantes :

    * code (servant de clé unique)
    * nom du produit
    * Quantité
    * Fabriquant
    * Point de vente (non exhaustif)
    * Nutriscore (a, b, c, d, e)
    * URL OpenFoodFacts de la page produit

Si le nutriscore est différent de "a" il recherche automatiquement un produit de score "a", sinon de score "b", etc.

Pour cela le programme récupère les mots clés à partir du nom générique du produit ou du nom du produit pour effectuer une nouvelle recherche avec un meilleur score.

Le programme intègre une seule base de données pour l'enregistrement sur demande utilisateur des produits de substitution trouvés.

**Remarque:** Utilisation de fichiers JSON pour les paramètres de connexion à la base de données et pour les catégories principales.

## Difficultés

La base de données OpenFoodFacts n'est pas forcément très bien remplie, ce qui pose problème pour effectuer des recherches par noms, noms génériques, catégories...

Le plus dur est donc de pouvoir afficher des produits de substitution qui correspondent au produit initial.
