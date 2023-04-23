print("Google Travel Planner\n")
# Samm 1: Arvutage kahe linna vaheline reisiaeg.
kaugus = float(input("Sisesta linnadevaheline kaugus kilomeetrites: "))
kiirus = float(input("Sisesta keskmine kiirus kilomeetrites tunnis: "))
reisiaeg = kaugus / kiirus
tunnid = int(reisiaeg)
minutid = int((reisiaeg - tunnid) * 60)
print("Reisiaeg: " + str(tunnid) + " tundi ja " +  str(minutid) + " minutit.\n")

# Samm 2: Arvutage reisi maksumus.
piletihind = float(input("Sisesta kahe linna vahelise üksikpileti hind eurodes: "))
edasi_tagasi = input("Kas te soovite edasi-tagasi piletit? (kui JAH - sisesta 2, kui EI - sisesta 1):")
reisi_maksumus = float(piletihind) * float(edasi_tagasi)
print("Reisi maksumus on: {:.2f} eurot.\n".format(reisi_maksumus))

# Samm 3: Planeerige reisi kestus.
vaatamisväärsuse_päevad = int(input("Sisesta päevade arv, mille jooksul soovite vaatamisväärsustega tutvuda: "))
puhkuse_päevad = int(input("Sisesta päevade arv, mida soovite veeta puhkusel: "))
reisi_kestus = vaatamisväärsuse_päevad + puhkuse_päevad
print("Terve reisi kestus on: " + str(reisi_kestus) + " päeva.\n")

# Samm 4: Planeeri igapäevaseid tegevusi.
#ärkamis_tund, ärkamis_minut = map(int, input("Enter your wake-up time (hour and minute, separated by a space): ").split())
ärkamis_tund = int(input("Sisesta oma ärkamistund: "))
ärkamis_minut = int(input("Sisesta oma ärkamisminutid: "))
vaatamisväärsuse_tunnid = int(input("Sisesta tundide arv, mille jooksul soovitee vaatamisväärsusi külastada: "))
puhkuse_tunnid = int(input("Sisesta tundide arv, mida soovite veeta puhkamiseks: "))
lõpp_tund = (ärkamis_tund + vaatamisväärsuse_tunnid + puhkuse_tunnid) % 24
lõpp_minut = ärkamis_minut
print("Teie päev lõpeb kell {:02d}:{:02d}\n".format(lõpp_tund, lõpp_minut))

# Samm 5: Arvutage reisi kogumaksumus.
söögi_maksumus = float(input("Sisesta söögi päevane maksumus eurodes: "))
majutuse_maksumus = float(input("Sisesta majutuse maksumus öö kohta eurodes: "))
söögi_kogumaksumus = söögi_maksumus * reisi_kestus #samm3
majutuse_kogumaksumus = majutuse_maksumus * reisi_kestus #samm3
reisi_kogumaksumus = söögi_kogumaksumus + majutuse_kogumaksumus + reisi_maksumus #samm2
print("Reisi kogumaksumus: {:.2f} eurot.".format(reisi_kogumaksumus))