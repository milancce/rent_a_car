from datetime import datetime

import pymysql


class DB:
    def __init__(self):
        self.__connection = pymysql.connect(host='localhost', user='pyuser', password='py123', db='oop3', port=3306,
                                            charset='utf8', cursorclass=pymysql.cursors.DictCursor)
        if self.__connection:
            print("Connected")

    def _get_connection(self):
        return self.__connection

    def prikazi_korisnike(self):
        cursor = self.__connection.cursor()
        cursor.execute("SELECT * FROM users")  # Nema args
        for row in cursor.fetchall():
            print(row)
        cursor.close()

    def prikazi_vozila(self):
        cursor = self.__connection.cursor()
        cursor.execute("SELECT * FROM cars")
        for row in cursor.fetchall():
            print(row)
        cursor.close()

    def prikazi_rentirana(self):
        cursor = self.__connection.cursor()
        cursor.execute("SELECT * FROM reservations r JOIN cars c ON r.id_car=c.id")
        for row in cursor.fetchall():
            print(f"{row['brand']} {row['model']} {row['production_year']} "
                  f"{row['start_date'].strftime('%Y-%m-%d %H:%M:%S')} "
                  f"{row['end_date'].strftime('%Y-%m-%d %H:%M:%S')} "
                  f"do kraja rezervacije ostalo: {row['end_date'] - datetime.now()}")
        cursor.close()
