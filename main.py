
from models.Users import User
from models.DB import *
from models.Reservation import Reservation
from models.Car import *


option=None

korisnik=None



db=DB()

while option!="":
    print("1.Dodaj korisnika \n 2.Prikazi korisnike \n3.Rezervisi vozilo \n4.Prikazi raspoloziva vozila \n 5.Prikazi rentirana vozila\n")
    option=input("Unesi izbor:")
    if option=="1":
        name=input("Unesi ime (npr. Milan Crnomarkovic):")
        godine=input("Unesi ime (npr. 22):")

        korisnik=User(name=name,godine=int(godine))
    elif option=="2":
         db.prikazi_korisnike()
    elif option=="3":
        if korisnik is None:
            raise IOError("Niste uneli korisnika!")
        else:
            db.prikazi_vozila()
            id_vozila=input("Unesi id vozila:")
            start_date=input("Unesi pocetak datuma i vreme od kog zelite da rentirate vozilo (npr. 2025-12-19 13:45:00)")
            end_date=input("Unesite kraj datuma i vreme do kog zelite da rentirate vozilo (npr. 2025-12-19 19:45:00) ")

            rezervacija=Reservation()
            rezervacija.id_car=id_vozila
            rezervacija.id_user=korisnik.id
            rezervacija.start_date=start_date
            rezervacija.end_date=end_date

            rezervacija.proveri_rezevaciju()

    elif option=="4":
        db.prikazi_vozila()
    elif option=="5":
        db.prikazi_rentirana()








