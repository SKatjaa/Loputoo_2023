def main():
    tooted = {
        "õun": {"hind": 0.79, "kogus": 10},
        "banaan": {"hind": 1.20, "kogus": 15},
        "apelsin": {"hind": 1.99, "kogus": 20},
        "viinamari": {"hind": 3.29, "kogus": 5},
        "arbuus": {"hind": 3.99, "kogus": 2},
        "ananass": {"hind": 2.49, "kogus": 7},
        "kiivi": {"hind": 3.49, "kogus": 12},
        "pirn": {"hind": 1.49, "kogus": 8},
        "maasikas": {"hind": 7.99, "kogus": 50},
        "mango": {"hind": 4.99, "kogus": 4}
    }

    ostukorv = []

    while True:
        print("\nTere tulemast Amazoni!")
        print("Mina olen Teie isiklik ostuassistent. Kuidas saan aidata teile täna?!")
        print("Valige mida soovite teha!")
        print("1. Otsida toode")
        print("2. Lisada toode ostukorvi")
        print("3. Vaadata oma ostukorvi")
        print("4. Eemaldada toode ostukorvist")
        print("5. Vaadata hind kokku")
        print("6. Vormistada tellimus")
        print("7. Väljuda")

        valik = input("Sisestage oma valik: ")

        if valik == "1":
            otsi_toode(tooted)
        elif valik == "2":
            lisada_ostukorvi(tooted, ostukorv)
        elif valik == "3":
            vaadata_ostukorvi(ostukorv)
        elif valik == "4":
            eemaldada_ostukorvist(tooted,ostukorv)
        elif valik == "5":
            vaadata_hind_kokku(ostukorv)
        elif valik == "6":
            checkout(tooted,ostukorv)
        elif valik == "7":
            print("Aitäh, et ostate Amazoniga!")
            break
        else:
            print("Vabandust, ma ei saanud sellest aru. Palun proovige uuesti!")

def otsi_toode(tooted):
    otsingusõna = input("\nSisestage otsingusõna: ")
    sobib = {}
    for toode, detailid in tooted.items():
        if otsingusõna.lower() in toode.lower():
            sobib[toode] = detailid
    print("Las ma vaatan, kas meil on see toode saadaval!")
    if sobib:
        print("Otsingu tulemused: ")
        for toode, detailid in sobib.items():
            print(str(toode) + " - €" + str(detailid['hind']) + " [" + str(detailid['kogus']) + " on saadaval]")

    else:
        print("Ma ei leidnud ühtegi vastet.")

def lisada_ostukorvi(tooted,ostukorv):
    toode = input("\nSisestage selle toote nimi, mida soovite ostukorvi lisada: ")
    if toode not in tooted:
        print("Toode ei leitud.")
        return
    kogus = input("Hea valik! Kui palju soovite?: ")
    try:
        kogus = int(kogus)
        if kogus <= 0:
            print("Vale kogus.Palun proovige uuesti!")
            return
    except ValueError:
        print("Vale kogus.Palun proovige uuesti!")
        return
    if kogus > tooted[toode]["kogus"]:
        print("Vabandage! Meil puudub piisav kogus.")
        return
    tooted[toode]["kogus"] -= kogus
    ostukorv.append((toode, tooted[toode]["hind"], kogus))
    print(str(kogus) +" "+ str(toode)+" lisati ostukorvi.")

def vaadata_ostukorvi(ostukorv):
    if not ostukorv:
        print("\nTeie ostukorv on tühi.")
        return
    print("\nTeie ostukorv: ")
    for item in ostukorv:
        print("{} (€{:.2f}) x{}".format(item[0], item[1], item[2]))
        
def eemaldada_ostukorvist(tooted,ostukorv):
    toode = input("\nSisestage selle toote nimi, mida soovite ostukorvist eemaldada: ")
    for item in ostukorv:
        if item[0] == toode:
            tooted[toode]["kogus"] += item[2]
            ostukorv.remove(item)
            print("{} {} eemaldati ostukorvist.".format(item[2], tooted[toode]['kirjeldus']))
            return
    print("Toode ei leitud ostukorvis.")
    
def vaadata_hind_kokku(ostukorv):
    hind_kokku = sum(item[1]*item[2] for item in ostukorv)
    print("\nTeie ostukorvi hind kokku: €{:.2f}".format(hind_kokku))

def checkout(tooted,ostukorv):
    if not ostukorv:
        print("\nTeie ostukorv on tühi.")
        return
    hind_kokku = sum(item[1]*item[2] for item in ostukorv)
    print("\nHind kokku: €{:.2f}".format(hind_kokku))
    kindel = input("Kas olete kindel, et soovite tellimuse vormistada? (jah/ei) ")
    if kindel.lower() == "jah":
        for item in ostukorv:
            tooted[item[0]]["kogus"] -= item[2]
        ostukorv.clear()
        print("Täname teid ostu eest!")
    else:
        print("Tellimuse vormistamine on tühistatud.")

main()
