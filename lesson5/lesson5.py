import csv
import json
import os

def sisendtehing():
    kuupäev = input("Sisestage kuupäev (YYYY-MM-DD): ")
    kategoorija = input("Sisestage kategoorija (tulu/kulu/investeering): ")
    summa = float(input("Sisestage summa: "))
    return kuupäev, kategoorija, summa

def salvesta_tehing_csv_faili(tehing, csv_filename="transactions.csv"):
    with open(csv_filename, "a", newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(tehing)

def analüüsi_tehinguid(alguskuupäev, lõppkuupäev, csv_filename="transactions.csv"):
    sissetulek_kokku = 0
    kulud_kokku = 0
    investeeringud_kokku = 0

    with open(csv_filename, "r", newline='') as csvfile:
        csv_reader = csv.reader(csvfile)
        for row in csv_reader:
            kuupäev, kategoorija, summa = row
            if alguskuupäev <= kuupäev <= lõppkuupäev:
                if kategoorija == "tulu":
                    sissetulek_kokku += float(summa)
                elif kategoorija == "kulu":
                    kulud_kokku += float(summa)
                elif kategoorija == "investeering":
                    investeeringud_kokku += float(summa)

    return sissetulek_kokku, kulud_kokku, investeeringud_kokku

def salvesta_analüüsitud_andmed_json_faili(sissetulek_kokku, kulud_kokku, investeeringud_kokku, \
                               kuupäeva_vahemik, json_failinimi="analyzed_data.json"):
    analyzed_data = "Kuupäeva vahemik: " + str(kuupäeva_vahemik) + "\n\
" + "Sissetulek kokku: " + str(sissetulek_kokku) + "\n\
" + "Kulud kokku: " + str(kulud_kokku) + "\n\
" + "Investeeringud kokku: " + str(investeeringud_kokku)
    with open(json_failinimi, "w") as jsonfile:
        jsonfile.write(analyzed_data)
        
def json_fail_on_olemas(json_failinimi):
    return os.path.exists(json_failinimi)

def main():
    if not os.path.exists("transactions.csv"):
        with open("transactions.csv", "w", newline=''):
            pass

    while True:
        print("\nValikud:")
        print("1. Lisa tehing")
        print("2. Analüüsida tehinguid")
        print("3. Salvesta analüüsitud tehingud json-faili")
        print("4. Välju")
        valik = int(input("Valige valik (1-4): "))

        if valik == 1:
            tehing = sisendtehing()
            salvesta_tehing_csv_faili(tehing)
            
        elif valik == 2:
            alguskuupäev = input("Sisestage alguskuupäev (YYYY-MM-DD): ")
            lõppkuupäev = input("Sisestage lõppkuupäev (YYYY-MM-DD): ")
            sissetulek_kokku, kulud_kokku, investeeringud_kokku = analüüsi_tehinguid(alguskuupäev, lõppkuupäev)
            print("Sissetulek kokku: "+str(sissetulek_kokku))
            print("Kulud kokku: "+str(kulud_kokku))
            print("Investeeringud kokku: "+str(investeeringud_kokku))
            
        elif valik == 3:
            salvesta_analüüsitud_andmed_json_faili(sissetulek_kokku, kulud_kokku, investeeringud_kokku, (alguskuupäev, lõppkuupäev))
            if json_fail_on_olemas("analyzed_data.json"):
                print("Andmed on edukalt salvestatud faili 'analyzed_data.json'.")
            else:
                print("Midagi läks valesti.")
                
        elif valik == 4:
            print("Väljumine...")
            break
        else:
            print("Vale valik. Palun proovige uuesti.")
main()