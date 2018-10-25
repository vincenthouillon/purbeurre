import json

import mysql.connector
import requests

from config import configuration as conf


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
                product_name VARCHAR(140) NOT NULL,
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
            CREATE UNIQUE INDEX UK_code ON Records (code);
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
            INSERT INTO Records(code, product_name, quantity, brand, store,
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

def main():
    from configuration import url_product
    db = Dbase
    db.create_tbl_recording()

if __name__ == '__main__':
    main()