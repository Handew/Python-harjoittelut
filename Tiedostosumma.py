print("Aloitetaan tiedoston käsittely.")

tiedosto = open("Luvut.txt", "r", encoding="utf8")
#data = tiedosto.read()
#print(data)

lukujen_summa = 0
rivi_nro = 1
for rivi in tiedosto:
    print(str(rivi_nro) + ": " + rivi)
    rivi_nro += 1
    lukujen_summa += int(rivi)

tiedosto.close()

print("Tiedostosta luettujen lukujen summa: ")
print(lukujen_summa)
print()
print("Suoritus päättyy.")