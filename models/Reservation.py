from datetime import datetime

from models.DB import DB


class Reservation(DB):
    def __init__(self):
        super().__init__()
        self.con = super()._get_connection()

        self.__id_car = None
        self.__id_user = None

        self.__start_date = None
        self.__end_date = None

    @property
    def id_car(self):
        return self.__id_car

    @property
    def id_user(self):
        return self.__id_user

    @property
    def start_date(self):
        return self.__start_date

    @property
    def end_date(self):
        return self.__end_date

    @id_car.setter
    def id_car(self, id_car):
        self.__id_car = id_car

    @id_user.setter
    def id_user(self, id_user):
        self.__id_user = id_user

    @start_date.setter
    def start_date(self, start_date):
        self.__start_date = start_date

    @end_date.setter
    def end_date(self, end_date):
        self.__end_date = end_date

    def dodaj_rezervaciju(self):
        insert_query = "INSERT INTO reservations (id_car,id_user,start_date,end_date) VALUES (%s,%s,%s,%s)"
        cursor = self.con.cursor()
        cursor.execute(insert_query, (self.__id_car, self.__id_user, self.__start_date, self.__end_date))
        self.con.commit()
        print("USPESNO NAPRAVLJENA REZERVACIJA")
        cursor.close()

    def proveri_tabelu(self):
        cursor = self.con.cursor()
        prazna_tabela = "SELECT * FROM reservations"
        cursor.execute(prazna_tabela)
        broj_redova = cursor.rowcount
        cursor.close()
        return broj_redova

    def proveri_rezevaciju(self):
        cursor = self.con.cursor()
        self.__start_date = datetime.strptime(self.__start_date, "%Y-%m-%d %H:%M:%S")
        self.__end_date = datetime.strptime(self.__end_date, "%Y-%m-%d %H:%M:%S")

        if self.__start_date > self.__end_date:
            raise IOError("Ne staviti pocetak rezervacije posle kraja")
        elif self.__start_date < datetime.now() or self.__end_date < datetime.now():
            raise IOError("Ne mozes rezervisati vozilo pre danasnjeg datuma")

        if self.proveri_tabelu() == 0:
            self.dodaj_rezervaciju()
        else:
            provera_query = "SELECT * FROM reservations where id_car=%s"

            cursor.execute(provera_query, (self.__id_car))
            reservations = cursor.fetchall()
            nema = True

            for reservation in reservations:
                if not (self.__end_date <= reservation["start_date"]
                        or self.__start_date >= reservation["end_date"]):
                    nema = False
                    break
            if nema:
                self.dodaj_rezervaciju()
            else:
                raise IOError("To vozilo je vec rezervisano tad!")

        cursor.close()
