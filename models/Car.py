cars = {
    "audi": [{"model": "A4", "godiste": 2004}, {"model": "A5", "godiste": 2003}, {"model": "A6", "godiste": 2002}]
    ,
    "bmw": [{"model": "M3", "godiste": 2013}, {"model": "M4", "godiste": 2001}, {"model": "M5", "godiste": 2021}],
    "mercedes": [{"model": "GLK", "godiste": 2016}, {"model": "GLE", "godiste": 2011},
                 {"model": "SLK", "godiste": 2015}]
}


class Car:
    def __init__(self):
        self.__brend = None
        self.__model = None
        self.__production_year = None

    @property
    def model(self):
        return self.__model

    @property
    def production_year(self):
        return self.__production_year

    @model.setter
    def model(self, model):
        if self.__brend is None:
            raise ValueError("That model does not exist")
        else:

            for car in cars[self.__brend]:
                if car["model"] == model:
                    self.__model = model
                    self.__production_year = car["godiste"]
                    break

            if self.__model is None:
                raise ValueError("That model does not exist")

    @property
    def brend(self):
        return self.__brend

    @brend.setter
    def brend(self, brend):
        if brend in cars:
            self.__brend = brend
        else:
            raise ValueError("That car brand does not exist")

    @property
    def production_year(self):
        return self.__production_year
