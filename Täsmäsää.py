import http.client
import sqlite3

connSQL = sqlite3.connect('paikkakunnat.db')
sql = "CREATE TABLE IF NOT EXISTS paikkakunnat (paikkakunta text)"
kursori = connSQL.cursor()
kursori.execute(sql)


kysely = input("Haluatko muuttaa seurattavia paikkakuntia? (K/E)    ")

if kysely == "K":
    while True:
        paikkakunta = input("Minkä paikkakunnan säätä haluat seurata? Kysely päättyy X vastauksella  ")
        if paikkakunta == "X":
            break
        sql = f'INSERT INTO paikkakunnat VALUES ("{paikkakunta}")'
        kursori.execute(sql)
        connSQL.commit()

kysely = input("Haluatko hakea lämpötilatiedot ilmatieteenlaitokselta? (K/E) ")
if kysely == "K":
    sql = "SELECT paikkakunta FROM paikkakunnat"
    for rivi in kursori.execute(sql):
        strMuunnos = (str(rivi))
        puhdasPaikkakunta = strMuunnos[2:-3]
        print(puhdasPaikkakunta)
        

connSQL.close

# conn = http.client.HTTPSConnection("www.ilmatieteenlaitos.fi")
# conn.request("GET", "/saa/porvoo")
# vastaus = conn.getresponse()
# html = str(vastaus.read())

# print(html[:500])
# indeksi = html.index('div class="temperature positive')
# alku = indeksi+78
# loppu = alku+2
# lämpötila = html[alku:loppu]
# print(f"Lämpötila Porvoossa: {lämpötila} astetta.")