import json

import requests
import mysql.connector

from progressbar import progress


# def get_categories():
#     """Recovering categories on OpenFoodFacts

#     Returns:
#         json -- all categories
#     """
#     print("Please wait, login to 'https://fr.openfoodfacts.org/categories.json'")
#     url = "https://fr.openfoodfacts.org/categories.json"
#     response = requests.get(url).json()
#     print("Successful connection\n")

#     counter = 0
#     for _ in response["tags"]:
#         progress(counter, response['count'],
#                  f"Recover all categories : {response['count']}")
#         counter += 1
#     print("")

#     openfoodfacts_categories = json.dumps(response)
#     return openfoodfacts_categories


def sql_connect():
    with open("db_params.json") as f:
        db_params = json.load(f)

    conn = mysql.connector.connect(
        **db_params['dbase'])

    return conn


def create_tbl_categories():
    dbase = sql_connect()
    cursor = dbase.cursor()
    cursor.execute("USE purbeurre;")
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Categorie (
            id INT(2) NOT NULL AUTO_INCREMENT,
            name VARCHAR(140) NOT NULL,
            PRIMARY KEY(id)
            )
            ENGINE=InnoDB
            DEFAULT CHARSET = utf8 COLLATE utf8_unicode_ci;
    """)


def read_categories():
    with open("main_categories.json", encoding="utf-8") as f:
        json_categories = json.load(f)
        return json_categories


def insert_categories():
    categories = read_categories()

    conn = sql_connect()
    cursor = conn.cursor()
    cursor.execute("USE purbeurre")

    for category in categories["ls_categories"]:
        cursor.execute("""
            INSERT INTO Categorie (name)
            VALUES ("{}")""".format(category))

    conn.commit()
    cursor.close()
    conn.close()


def url_categories(category, page=1):
    url = ("https://fr.openfoodfacts.org/cgi/search.pl?action=process&tagtype_0=categories&tag_contains_0=contains&tag_0={}&sort_by=unique_scans_n&page_size=20&axis_x=energy&axis_y=products_n&action=display&page={}&json=1").format(
        category, page)
    return url


def url_product(code):
    pass


def main():
    create_tbl_categories()
    # insert_categories()


if __name__ == '__main__':
    main()
