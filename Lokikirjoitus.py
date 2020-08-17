import datetime

def kirjoita_lokiin(viesti):
    aika = datetime.datetime.now()
    tiedosto = open("C:\\Users\\Hannu\\Python\Loki.txt", "a")
    rivi = str(aika) + " " + viesti
    tiedosto.write(rivi + "\r\n")
    tiedosto.close()
    print(rivi)

kirjoita_lokiin("Sovellus alkaa.")
kirjoita_lokiin("Testiä...")
kirjoita_lokiin("Suoritus päättyy")