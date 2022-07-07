import csv     #### Klant #feedback:Klantgui: Maak een apart bestand met daarin de Class definitie voor het object.
               #### (nieuweklant.py gemaakt nav klant.py(ISBR))


class Klant:
    def __init__(self):
        self._naam = ''
        self._adres = ''
        self._postcode = ''
        self._woonplaats = ''
        self._land = ''
    
    def setnaam(self, naam): 
        self._naam = naam

    def getnaam(self):
        return self._naam
    
    naam = property(getnaam, setnaam)

    def setadres(self, adres):
        self._adres = adres

    def getadres(self):
        return self._adres
    
    adres = property(getadres, setadres)

    def setpostcode(self, postcode):
        self._postcode = postcode

    def getpostcode(self):
        return self._postcode
    
    postcode = property(getpostcode, setpostcode)

    def setwoonplaats(self, woonplaats):
        self._woonplaats = woonplaats

    def getwoonplaats(self):
        return self._woonplaats

    woonplaats = property(getwoonplaats, setwoonplaats)

    def setland(self, land):
        self._land = land


    def getland(self):
        return self._land
    
    land = property(getland, setland)


def readklant():
    with open('Klanten.csv') as csv_file:
        csv_lijst = csv.reader(csv_file, delimiter=',')
        klanten = []
        for row in csv_lijst:
            klant_object = Klant()
            klant_object.naam = row[0]
            klant_object.adres = row[1]
            klant_object.postcode = row[2]        
            klant_object.woonplaats = row[3]
            klant_object.land = row = [4]
           
            klanten.append(row)
    return klanten
