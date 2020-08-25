import http.client
import sqlite3
import requests
import datetime

kpl = 0
aika = datetime.datetime.now()

def loki_onnistunut(viesti):
    tiedosto = open("Loki.txt", "a")
    
    rivi = str(aika) + " " + "Haettiin onnistuneesti "+str(kpl)+ " paikkakunnan lämpötilat"
    tiedosto.write(rivi + "\r\n")
    tiedosto.close()

def loki_virhe(viesti):
    tiedosto = open("Loki.txt", "a")

    virhe = f"{viesti} -Hakuvirhe"
    rivi = str(aika) + " " +virhe
    tiedosto.write(rivi + "\r\n")   
    tiedosto.close()

connSQL = sqlite3.connect('paikkakunnat.db')
sql = "CREATE TABLE IF NOT EXISTS paikkakunnat (paikkakunta text)"
kursori = connSQL.cursor()
kursori.execute(sql)

print("Tervetuloa paikkakuntakohtaiseen sääpalveluun. Ohjelmaversio 1.0")
print()
print()

kysely = input("Haluatko muuttaa seurattavia paikkakuntia? (K/E)    ")
print()

if kysely == "K":
    while True:
        paikkakunta = input("Minkä paikkakunnan säätä haluat seurata? Kysely päättyy X vastauksella  ")
        if paikkakunta == "X":
            print()
            break
        sql = f'INSERT INTO paikkakunnat VALUES ("{paikkakunta}")'
        kursori.execute(sql)
        connSQL.commit()

kysely = input("Haluatko hakea lämpötilatiedot ilmatieteenlaitokselta? (K/E) ")
print()
if kysely == "K":
    sql = "SELECT paikkakunta FROM paikkakunnat"
    for rivi in kursori.execute(sql):
        strMuunnos = (str(rivi))
        puhdasPaikkakunta = strMuunnos[2:-3]
        
        url = f"Https://www.ilmatieteenlaitos.fi/saa/{puhdasPaikkakunta}"
        vastaus = requests.get(url, params={"encoding": "utf-8"})
        vastaus_status = vastaus.status_code

        if vastaus_status == 200:
            html = str(vastaus.text)
            indeksi = html.index('span class="temperature-plus')
            alku = indeksi+46
            loppu = alku+2
            lämpötila = html[alku:loppu]
            print(f"Lämpötila {puhdasPaikkakunta}: {lämpötila} astetta.")
            kpl += 1
        else:
            loki_virhe(puhdasPaikkakunta)

    loki_onnistunut(puhdasPaikkakunta)

connSQL.close()

print()
print("Ohjelman suoritus päättyy.")