from DB import *
class User(DB):
    def __init__(self,name,godine):

        super().__init__()

        con=super()._get_connection()
        print(con)

        if len(name)<3 or godine<18:
            raise ValueError("Ime mora imati minimum 3 karaktera i korisnik mora biti punoletan!")
        self.__name=name
        self.__godine=godine

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self,name):
        if len(name) < 3:
            raise ValueError("Ime mora imati minimum 3 karaktera")
        self.__name=name

    @property
    def godine(self):
        return self.__godine

    @godine.setter
    def godine(self,godine):
        if godine < 18:
            raise ValueError("Korisnik mora biti punoletan")
        self.__godine=godine

toma=User("Tomislav",18)



