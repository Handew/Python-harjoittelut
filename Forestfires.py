tiedosto = open("forestfires.csv", "r")

rivinumero = 1

viikonpäivät = []

for rivi in tiedosto:
    if rivinumero > 1:
        viikonpäivä = rivi[8:11]
        viikonpäivät.append(viikonpäivä)

    rivinumero += 1

tiedosto.close()

#Tulosten näyttäminen
print(f"Tulokset {rivinumero} rivin käsittelyn jälkeen:")
print(f"Mon: {viikonpäivät.count('mon')}")
print(f"Tue: {viikonpäivät.count('tue')}")
print(f"Wed: {viikonpäivät.count('wed')}")
print(f"Thu: {viikonpäivät.count('thu')}")
print(f"Fri: {viikonpäivät.count('fri')}")
print(f"Sat: {viikonpäivät.count('sat')}")
print(f"Sun: {viikonpäivät.count('sun')}")