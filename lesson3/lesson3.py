import random

print("Tere tulemast seiklusmängu!")
print("Sul on 7 käiku, et jõuda aardeni ja võita mäng.")
print("Edu!\n")

käiku_jäänud = 7
aare_leitud = False
etapp = 1

while käiku_jäänud > 0 and not aare_leitud:
    print("Käiku jäänud: " + str(käiku_jäänud))

    if etapp == 1:
        print("\nSa seisad metsas. Saad liikuda põhja, lõuna, itta või läände.")
        suund = input("Sisesta suund, mida soovid liikuda (põhja, lõuna, ida, lääs): ")
        käiku_jäänud -= 1
        if suund.lower() == "ida":
            etapp = 2
        else:
            print("Vale suund! Proovi uuesti.")

    elif etapp == 2:
        print("\nOled jõudnud jõe äärde. Saad ujuda üle, ehitada parve või leida silla.")
        valik = input("Sisesta oma valik (ujuda, parv, sild): ")
        käiku_jäänud -= 1
        if valik.lower() == "sild" or valik.lower() == "parv":
            etapp = 3
        else:
            print("Vale valik! Proovi uuesti.")

    elif etapp == 3:
        print("\nSa ületasid jõe. Nüüd oled teelahkmel. Võid minna vasakule või paremale.")
        valik = input("Sisesta oma valik (vasakule, paremale): ")
        käiku_jäänud -= 1
        if valik.lower() == "vasakule":
            etapp = 4
        else:
            print("Vale valik! Proovi uuesti.")

    elif etapp == 4:
        print("\nOled jõudnud salakoodiga ukseni. Kood on täisarv vahemikus 1 kuni 10. Sul on 5 katset.")
        salakood = random.randint(1, 10)
        katset_jäänud = 5
        while katset_jäänud > 0:
            koodi_oletus = int(input("Sisesta oma oletus salakoodi kohta: "))
            if koodi_oletus == salakood:
                print("\nÕige! Uks avaneb.")
                print("Sa leidsid aarde! Palju õnne!")
                aare_leitud = True
                break
            else:
                katset_jäänud -= 1
                print("Vale oletus. Sul on jäänud " + str(katset_jäänud) +" katset.\n")
        etapp = 5

    else:
        break

if aare_leitud:
    print("Sa võitsid mängu!")
elif käiku_jäänud <= 0:
    print("\nOlete teinud liiga palju käiku! Mäng lõppenud.")
else:
    print("\nSa kaotasid mängu.")