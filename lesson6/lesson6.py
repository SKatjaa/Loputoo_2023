import random

def lisa_laul(esitusloend):
    pealkiri = input("\nSisestage laulu pealkiri: ")
    artist = input("Sisestage artisti nimi: ")
    kestus = input("Sisestage laulu kestus (sekundites): ")
    esitusloend.append([pealkiri, artist, kestus])
    print("Esitusloendisse lisati "+str(pealkiri)+" ("+str(kestus)+" s), "+str(artist)+".")

def eemalda_laul(esitusloend):
    pealkiri = input("\nSisestage laulu pealkiri, et eemaldada: ")
    for laul in esitusloend:
        if laul[0] == pealkiri:
            esitusloend.remove(laul)
            print(str(pealkiri)+" on eemaldatud esitusloendist.")
            return
    print(str(pealkiri)+" ei ole esitusloendis.")

def sort_esitusloend(esitusloend):
    sort_järgi = input("\nSorteerida (pealkiri/artist/kestus) järgi: ")
    if sort_järgi == "pealkiri":
        esitusloend.sort()
    elif sort_järgi == "artist":
        esitusloend.sort(key=lambda laul: laul[1])
    elif sort_järgi == "kestus":
        esitusloend.sort(key=lambda laul: int(laul[2]))
    else:
        print("Vale sorteerimiskriteerium.")
        return
    print("Esitusloend on sorteeritud "+str(sort_järgi)+" järgi.")

def kuva_esitusloend(esitusloend):
    if not esitusloend:
        print("\nEsitusloend on tühi.")
        return
    print("\nLaulude arv esitusloendis:", len(esitusloend))
    print("Esitusloend:")
    for i, laul in enumerate(esitusloend):
        print(str(i+1) + ". " + laul[0] + ", " + laul[1] + " (" + str(laul[2]) + "s).")

def salvesta_esitusloend(esitusloend):
    failinimi = input("\nSisestage failinimi, et salvestada esitusloend: ")
    with open(failinimi, "w") as fail:
        for laul in esitusloend:
            fail.write(",".join(laul) + "\n")
    print("Esitusloend on salvestatud faili", failinimi)

def tühjenda_esitusloend(esitusloend):
    esitusloend.clear()
    print("\nEsitusloend on tühjendatud.")
    
def otsi_laul(esitusloend):
    otsingusõna = input("\nSisestage otsingusõna: ")
    sobib = []
    for laul in esitusloend:
        if otsingusõna.lower() in laul[0].lower() or otsingusõna.lower() in laul[1].lower() or otsingusõna == laul[2]:
            sobib.append(laul)
    if sobib:
        print("Leiti "+str(len(sobib))+" vastet:")
        for i, laul in enumerate(sobib):
            print(str(i+1) + ". " + laul[0] + ", " + laul[1] + " (" + str(laul[2]) + "s).")
    else:
        print("Ei leitud ühtegi vastet.")


def main():
    esitusloend = []

    while True:
        print("\nValikud:")
        print("1. Lisada laul")
        print("2. Eemalda laul")
        print("3. Sorteerida esitusloend")
        print("4. Kuva esitusloend")
        print("5. Salvesta esitusloend")
        print("6. Segada esitusloend")
        print("7. Tühjenda esitusloend")
        print("8. Otsida laul")
        print("9. Väljuda")
        valik = input("Sisestage oma valik (1-9): ")

        if valik == "1":
            lisa_laul(esitusloend)
        elif valik == "2":
            eemalda_laul(esitusloend)
        elif valik == "3":
            sort_esitusloend(esitusloend)
        elif valik == "4":
            kuva_esitusloend(esitusloend)
        elif valik == "5":
            salvesta_esitusloend(esitusloend)
        elif valik == "6":
            random.shuffle(esitusloend)
            print("\nEsitusloend on segatud.")
        elif valik == "7":
            tühjenda_esitusloend(esitusloend)
        elif valik == "8":
            otsi_laul(esitusloend)
        elif valik == "9":
            print("Väljumine...")
            break 
        else:
            print("Vale valik. Palun proovige uuesti.")

main()