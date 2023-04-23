class Robot:
    def __init__(self, nimi, aku_tase=100):
        self.nimi = nimi
        self.aku_tase = aku_tase

    def liikuda(self, sihtkoht):
        print(str(self.nimi)+" liigub. Tema sihtkoht on "+str(sihtkoht)+ "...")
        self.aku_tase -= 10

    def laadida(self):
        self.aku_tase = 100
        print(str(self.nimi) + "'i aku on laetud 100%-ni.") 

class Tarnerobot(Robot):
    def __init__(self, nimi, aku_tase=100):
        super().__init__(nimi, aku_tase)

    def tarnida_tellimus(self, saaja, sihtkoht):
        if self.aku_tase < 25:
            print("Tarne lõpetamisek ei ole piisavalt akut.")
            return
        self.liikuda(sihtkoht)
        print(str(self.nimi)+" on andnud paki "+str(saaja)+ " kätte.")
        self.aku_tase -= 25

    def skaneerida_paki(self, pakend):
        if self.aku_tase < 20:
            print("Skaneerimise lõpetamisek ei ole piisavalt akut.")
            return
        print(str(self.nimi)+" on skaneerinud pakendi: "+str(pakend))
        self.aku_tase -= 20

class Puhastusrobot(Robot):
    def __init__(self, nimi, aku_tase=100):
        super().__init__(nimi, aku_tase)
        self.puhastusrežiim = ""

    def vali_puhastusrežiim(self, režiim):
        self.puhastusrežiim = režiim
        
        if self.aku_tase < 22:
            print("Puhastamise lõpetamisek ei ole piisavalt akut.")
            return
        if self.puhastusrežiim == "pühkima":
            self.aku_tase -= 10
            print(str(self.nimi)+" pühib põrandat.")
        elif self.puhastusrežiim == "pesema":
            self.aku_tase -= 20
            print(str(self.nimi)+" peseb põrandat.")
        elif self.puhastusrežiim == "tolmuimeja":
            self.aku_tase -= 25
            print(str(self.nimi)+" puhastab vaipu tolmuimejaga.")
        else:
            print("Puhastusrežiimi ei ole valitud.")
            return

    def puhastada_tuba(self, tuba):
        if self.aku_tase < 10:
            print("Puhastamise lõpetamisek ei ole piisavalt akut.")
            return
        self.liikuda(tuba)
        print(str(self.nimi)+" puhastab "+str(tuba))
        self.aku_tase -= 10

    def laadida(self):
        self.aku_tase = 100
        print(str(self.nimi) + "'i aku on laetud 100%-ni.")


def main():
    
    while True:
        print("\nVali robot:")
        print("1. Tarnerobot (1)")
        print("2. Puhastusrobot (2)")
        print("3. Välju")
        valik = input("Sisestage valik: ")

        if valik == "1":
            nimi = input("Sisestage nimi oma tarneroboti jaoks: ")
            tarnerobot = Tarnerobot(nimi)
            while True:
                print("\nTarneroboti tegevused:")
                print("1. Tarnida pakend")
                print("2. Skaneerida pakend")
                print("3. Laadida aku")
                print("4. Tagasi peamenüüsse")
                tarne_valik = input("Sisestage valik: ")
                if tarne_valik == "1":
                    saaja = input("Sisestage saaja nimi: ")
                    sihtkoht = input("Sisestage tarne sihtkoht: ")
                    tarnerobot.tarnida_tellimus(saaja, sihtkoht)
                elif tarne_valik == "2":
                    pakend = input("Sisestage pakend, mis on vaja skaneerida: ")
                    tarnerobot.skaneerida_paki(pakend)
                elif tarne_valik == "3":
                    tarnerobot.laadida()
                elif tarne_valik == "4":
                    break
                else:
                    print("Vale valik.")

        elif valik == "2":
            nimi = input("Sisestage nimi oma puhastusroboti jaoks: ")
            puhastusrobot = Puhastusrobot(nimi)
            while True:
                print("\nPuhastusroboti tegevused:")
                print("1. Puhastada tuba")
                print("2. Vali puhastusrežiim")
                print("3. Laadida aku")
                print("4. Tagasi peamenüüsse")
                puhastus_valik = input("Sisestage valik: ")
                if puhastus_valik == "1":
                    tuba = input("Sisestage tuba te soovite puhastada: ")
                    puhastusrobot.puhastada_tuba(tuba)
                elif puhastus_valik == "2":
                    puhastusrežiim = input("Sisestage puhastusrežiim (pühkima, pesema, tolmuimeja): ")
                    puhastusrobot.vali_puhastusrežiim(puhastusrežiim)
                elif puhastus_valik == "3":
                    puhastusrobot.laadida()
                elif puhastus_valik == "4":
                    break
                else:
                    print("Vale valik.")
                    
        elif valik == "3":
            print("Väljumine...")
            break
        else:
            print("Vale käsk.")
            
main()
