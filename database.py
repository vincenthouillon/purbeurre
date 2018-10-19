import configuration
import json


class Dbase:
    def __init__(self):
        pass

    @staticmethod
    def show_databases():
        # ! For test !!!
        cnx = configuration.sql_connect()
        cursor = cnx.cursor()
        cursor.execute("""SHOW DATABASES;""")
        for x in cursor:
            yield(x)

    @staticmethod
    def drop_table(tbl_name):
        # ? Or truncate (O_o)
        cnx = configuration.sql_connect()
        cursor = cnx.cursor()
        cursor.execute("""DROP TABLE IF EXISTS Categories;""").format(tbl_name)

    @staticmethod
    def insert_categories():
        with open("main_categories.json", encoding="utf-8") as f:
            main_categories = json.load(f)

        cnx = sql_connect()
        cur = cnx.cursor()
        num = 0
        for value in main_categories:
        cur.execute("""
            INSERT INTO Categories(id, name)
            VALUES("%i", "%s");
        """) % (num, value)
        num += 1
        cur.commit()
        cur.close()


def main():
    db = Dbase()
    # ? For test !!
    for i in db.show_databases():
        print(i)


if __name__ == '__main__':
    main()
