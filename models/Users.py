import re

from models.DB import DB


class User(DB):

    def __init__(self, name, godine):
        super().__init__()

        self.con = super()._get_connection()
        self.proveri_unos(name, godine)
        self.__name = name
        self.__godine = godine
        self.__id = None
        self.provera_korisnika()

    def proveri_unos(self, name, godine):
        pattern = r"^[A-ZČĆŠŽĐ][a-zčćšžđ]+ [A-ZČĆŠŽĐ][a-zčćšžđ]+$"

        if not re.fullmatch(pattern, name):
            raise ValueError("Morate uneti ime i prezime (npr. Tomislav Nikolic)")

        if len(name) < 3 or godine < 18:
            raise ValueError("Ime mora imati minimum 3 karaktera i korisnik mora biti punoletan!")

    def provera_korisnika(self):
        cursor = self.con.cursor()
        query = "SELECT * FROM users WHERE godine=%s and name=%s"
        cursor.execute(query, (self.__godine, self.__name,))
        user = cursor.fetchone()
        if user:
            self.__id = user["id"]
        else:
            self.dodaj_korisnika()
        cursor.close()

    @property
    def name(self):
        return self.__name

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        self.__id = id

    @name.setter
    def name(self, name):
        if len(name) < 3:
            raise ValueError("Ime mora imati minimum 3 karaktera")
        self.__name = name

    @property
    def godine(self):
        return self.__godine

    @godine.setter
    def godine(self, godine):
        if godine < 18:
            raise ValueError("Korisnik mora biti punoletan")
        self.__godine = godine

    def dodaj_korisnika(self):
        # Korisnici mogu da imaju isto ime , nemamo parametar po kome bi ih razlikovali
        # Da radimo neki sajt ili nesto slicno tome razlikovali bi korisnike po korisnickom imenu ili emailu
        # Gledacemo idealni scenario da se svi zovu razlicito

        cursor = self.con.cursor()
        exist_user = "SELECT * FROM users where name=%s"
        cursor.execute(exist_user, (self.__name,))
        if cursor.rowcount > 0:
            raise IOError("Korisnik sa ovim imenom vec postoji")
        else:
            query = "INSERT INTO users (name,godine) VALUES (%s,%s)"
            cursor.execute(query, (self.__name, self.__godine,))
            self.__id = cursor.lastrowid
            self.con.commit()

        cursor.close()
