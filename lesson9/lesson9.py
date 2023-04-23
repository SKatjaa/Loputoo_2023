from abc import ABC, abstractmethod
from typing import List

class InstagramProfiil:
    def __init__(self, kasutajanimi: str, täisnimi: str,\
                 elulugu: str, jälgijad: int, following: int, postitused: int):
        self.kasutajanimi = kasutajanimi
        self.täisnimi = täisnimi
        self.elulugu = elulugu
        self.jälgijad = jälgijad
        self.following = following
        self.postitused = postitused

    def __str__(self):
        return "\n" + self.kasutajanimi + " (" + self.täisnimi + ") - " \
               + self.elulugu + "\njälgijad: " + str(self.jälgijad) + \
               ", Following: " + str(self.following) + ", postitused: " + str(self.postitused)

class AbstractKuvamine(ABC):
    @abstractmethod
    def kuva_profiilid(self, profiilid: List[InstagramProfiil]) -> None:
        pass

class LihtneKuvamine(AbstractKuvamine):
    def kuva_profiilid(self, profiilid: List[InstagramProfiil]) -> None:
        for profiil in profiilid:
            print(profiil)

class FancyKuvamine(AbstractKuvamine):
    def kuva_profiilid(self, profiilid: List[InstagramProfiil]) -> None:
        for profiil in profiilid:
            print("📸 " + profiil.kasutajanimi +\
                  " (" + profiil.täisnimi + ")\n" + "💬 " + profiil.elulugu + \
                  "\n" + "👥 Followers: " + str(profiil.jälgijad) + ", Following: " + \
                  str(profiil.following) + "\n" + "🖼 Posts: " + str(profiil.postitused) + "\n")
            
class InstagramRakendus:
    def __init__(self):
        self.profiilid = []
        self.kuvamine = LihtneKuvamine()

    def lisa_profiil(self, profiil: InstagramProfiil) -> None:
        self.profiilid.append(profiil)
        
    def muuda_profiil(self, muudetav_kasutajanimi):
        muudetav_profiil = None
        for profiil in self.profiilid:
            if profiil.kasutajanimi == muudetav_kasutajanimi:
                muudetav_profiil = profiil
                break

        if muudetav_profiil:
            uus_kasutajanimi = input("Sisestage uus kasutajanimi: ")
            uus_täisnimi = input("Sisestage uus täisnimi: ")
            uus_elulugu = input("Sisestage uus elulugu: ")

            muudetav_profiil.kasutajanimi = uus_kasutajanimi
            muudetav_profiil.täisnimi = uus_täisnimi
            muudetav_profiil.elulugu = uus_elulugu
            print("Profiili edukalt redigeeritud.")
        else:
            print("Profiili ei leitud.")
            
    def kustuta_profiil(self, kustutatav_kasutajanimi):
        kustutatav_profiil = None
        for profiil in self.profiilid:
            if profiil.kasutajanimi == kustutatav_kasutajanimi:
                kustutatav_profiil = profiil
                break

        if kustutatav_profiil:
            self.profiilid.remove(kustutatav_profiil)
            print("Profiil edukalt kustutatud.")
        else:
            print("Profiili ei leitud.")
  
    def kuva_profiilid(self) -> None:
        if len(self.profiilid) == 0:
            print("Profiili ei leitud.")
        else:
            self.kuvamine.kuva_profiilid(self.profiilid)

    def seadista_kuvamise_stiil(self, stiil: str) -> None:
        if stiil == "lihtne":
            self.kuvamine = LihtneKuvamine()
            print("Kuva stiil muutus edukalt!")
        elif stiil == "fancy":
            self.kuvamine = FancyKuvamine()
            print("Kuva stiil muutus edukalt!")
        else:
            print("Vale valik. Sisestage õige stiil")

def main():
    app = InstagramRakendus()

    while True:
        print("\nInstagram profiili haldamine")
        print("1. Lisa profiil")
        print("2. Muuta profiil")
        print("3. Kustuta profiil")
        print("4. Kuva profiilid")
        print("5. Muuta kuvamisstiil")
        print("6. Välju")
        valik = input("Sisestage oma valik: ")

        if valik == "1":
            kasutajanimi = input("Sisestage kasutajanimi: ")
            täisnimi = input("Sisestage täisnimi: ")
            elulugu = input("Sisestage profiili elulugu: ")
            jälgijad = int(input("Sisestage jälgijate arv: "))
            following = int(input("Sisestage 'following'-i arv: "))
            postitused = int(input("Sisestage postituste arv: "))

            profiil = InstagramProfiil(kasutajanimi, täisnimi, elulugu, jälgijad, following, postitused)
            app.lisa_profiil(profiil)
            print("Profiil on edukalt lisatud!")

        elif valik == "2":
            muudetav_kasutajanimi = input("Sisestage redigeeritava profiili kasutajanimi: ")
            app.muuda_profiil(muudetav_kasutajanimi)
    
        elif valik == "3":
            kustutatav_kasutajanimi = input("Sisestage kustutatava profiili kasutajanimi: ")
            app.kustuta_profiil(kustutatav_kasutajanimi)

        elif valik == "4":
            app.kuva_profiilid()

        elif valik == "5":
            stiil = input("Sisestage kuvamisstiil (lihtne või fancy): ")
            app.seadista_kuvamise_stiil(stiil)

        elif valik == "6":
            print("Nägemist!")
            break

        else:
            print("Vale valik. Palun proovige uuesti.")
main()