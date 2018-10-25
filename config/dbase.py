import json

import mysql.connector
import requests

from config import configuration as conf
from config import progressbar


class Dbase:

    @staticmethod
    def sql_connect():
        with open("./config/db_params.json") as f:
            db_params = json.load(f)

        conn = mysql.connector.connect(
            **db_params['dbase'])
        return conn

    def drop_table(self, tbl_name):

        cnx = self.sql_connect()
        cursor = cnx.cursor()
        cursor.execute("""DROP TABLE IF EXISTS Categories;""").format(tbl_name)

    @staticmethod
    def create_tbl_recording():
        dbase = Dbase.sql_connect()
        cursor = dbase.cursor()
        cursor.execute("USE purbeurre")
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Records (
                id INT NOT NULL AUTO_INCREMENT,
                code VARCHAR(140) NOT NULL,
                name VARCHAR(140) NOT NULL,
                quantity VARCHAR(80),
                brand VARCHAR(140),
                store VARCHAR(140),
                nutriscore VARCHAR(1) NOT NULL,
                url VARCHAR(140) NOT NULL,
                category VARCHAR(140) NOT NULL,
                PRIMARY KEY(id)
                )
                ENGINE=InnoDB
                DEFAULT CHARSET = utf8 COLLATE utf8_unicode_ci;
        """)
        cursor.execute("""
            CREATE UNIQUE INDEX UK_code ON Records (code)
        """)

    @staticmethod
    def insert_tbl_categories(code, category):
        # OPEN DATA
        # print(code, category)
        url = conf.url_product(code)
        r = requests.get(url).json()
        page = json.dumps(r)
        value = json.loads(page)
        # print(value["code"])

        cnx = Dbase.sql_connect()
        cur = cnx.cursor()
        cur.execute("USE purbeurre")
        cur.execute("""
            INSERT INTO Records(code, name, quantity, brand, store,
            nutriscore, url, category)
            VALUES(%s, %s, %s, %s, %s, %s, %s, %s); """,
                    (
                        value['code'],
                        value['product']['product_name_fr'],
                        value['product']['quantity'],
                        value['product']['brands'],
                        value['product']['stores'],
                        value['product']['nutrition_grades'],
                        f"https://fr.openfoodfacts.org/produit/{value['product']['code']}",
                        category
                    ))
        cnx.commit()
        cnx.close()

    # def create_tbl_off_categories(self):
    #     cnx = self.sql_connect()
    #     cur = cnx.cursor()
    #     cur.execute("USE purbeurre;")
    #     cur.execute("""
    #         CREATE TABLE IF NOT EXISTS Categories (
    #             id VARCHAR(140) NOT NULL,
    #             name VARCHAR(140) NOT NULL,
    #             url VARCHAR(140) NOT NULL,
    #             products  INT(6) NOT NULL,
    #             PRIMARY KEY(id)
    #             )
    #             ENGINE=InnoDB
    #             DEFAULT CHARSET = utf8 COLLATE utf8_unicode_ci;
    #     """)

    # def get_off_categories(self):
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

    #     with open("categories_off.json", "w", encoding="utf8") as f:
    #         f.write(json.dumps(response, ensure_ascii=False))

    def insert_off_categories(self, json_file):
        with open(json_file, encoding="utf-8") as f:
            off_categories = json.load(f)

        cnx = self.sql_connect()
        cur = cnx.cursor()

        for value in off_categories['tags']:
            cur.execute("""
                INSERT IGNORE INTO Categories(id, name, url, products)
                VALUES(%s, %s, %s, %s);
            """, (value['id'], value['name'], value['url'], value['products']))

        cnx.commit()
        cnx.close()

def main():
    from configuration import url_product
    from progressbar import progress
    db = Dbase
    db.create_tbl_recording()

if __name__ == '__main__':
    main()