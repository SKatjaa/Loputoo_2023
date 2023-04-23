import random

# Auto paraanetrid
maks_aku_laeng = 100  # kWh
maks_vahemaa = 500  # km
laadimiskulu = 0.2  # kWh/km
laadimiskiirus = 22 # kW

# Määrake funktsioon auto järelejäänud aku protsendi arvutamiseks
def aku_protsent(praegune_aku_laeng, maks_aku_laeng=maks_aku_laeng):
    return (praegune_aku_laeng / maks_aku_laeng) * 100

# Määrake funktsioon, mis arvutab vahemaa,
#mille auto saab järelejäänud laadimisega läbida
def vahemaa_jäänud(jäänud_aku_protsent, maks_vahemaa):
    return (jäänud_aku_protsent / 100) * maks_vahemaa

# Määrake funktsioon aja arvutamiseks,
#mis kulub teatud vahemaa läbimiseks teatud kiirusega
def reisi_aeg(vahemaa, kiirus):
    return vahemaa / kiirus

# Määrake funktsioon teatud vahemaa läbimiseks
#nõutava aku laengu arvutamiseks
def nõutav_aku_laeng(vahemaa, laadimiskulu):
    return vahemaa * laadimiskulu

# Määrake funktsioon laadimisaja arvutamiseks
def laadimisaeg(nõutav_aku_laeng, laadimiskiirus):
    return nõutav_aku_laeng / laadimiskiirus


print("Tere tulemast Tesla elektriautosse!")
print("Teie Tesla maksimaalne laeng on "+str(maks_aku_laeng)+" kWh \
ja täislaadimisega saab sõita kuni "+str(maks_vahemaa)+" km.\n")

# Põhifunktsioon
def main(praegune_aku_laeng):
    jäänud_aku_protsent = aku_protsent(praegune_aku_laeng, maks_aku_laeng)
    jäänud_vahemaa = vahemaa_jäänud(jäänud_aku_protsent, maks_vahemaa)
    print("Teie praegune aku protsent on "+str(jäänud_aku_protsent)+" %. \
Saate sõita umbes "+str(jäänud_vahemaa)+" km.")
    
    random_kiirus = random.randint(50, 100)
    võib_veel_sõita = reisi_aeg(jäänud_vahemaa, random_kiirus)
    print("Teie auto juhuslik kiirus on "+str(random_kiirus)+" km/h. \
Ülejäänud vahemaa läbimiseks kulub umbes {:.1f} tundi.\n".format(võib_veel_sõita))
    
    soovitud_kaugus = float(input("Kui kaugele soovite reisida (km)?: "))
    vajalik_laeng_soovitud_kauguseks = nõutav_aku_laeng(soovitud_kaugus, laadimiskulu)
    print("Vahemaa reisimiseks aku laeng peab olema \
"+str(vajalik_laeng_soovitud_kauguseks)+" kWh.")

    if vajalik_laeng_soovitud_kauguseks <= praegune_aku_laeng:
        print("Teil on piisavalt laengut "+str(soovitud_kaugus)+" km läbimiseks.")
    else:
        vajab_laadimist = laadimisaeg(vajalik_laeng_soovitud_kauguseks - \
                                      praegune_aku_laeng, laadimiskiirus)
        print("Soovitud "+str(soovitud_kaugus)+" km vahemaa läbimiseks \
vajab auto laadimist {:.1f} tundi.".format(vajab_laadimist))

main(70)