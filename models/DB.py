
import pymysql

class DB:
    def __init__(self):
        self.__connection = pymysql.connect(host='localhost',user='pyuser',password='py123',db='oop2',port=3306,charset='utf8')
        if self.__connection:
            print("Connected")



    def _get_connection(self):
        return self.__connection