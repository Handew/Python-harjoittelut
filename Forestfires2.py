tiedosto = open("forestfires.csv", "r")

rivinumero = 1

viikonpäivät = { "mon": 0, "tue": 0, "wed": 0, "thu": 0, "fri": 0, "sat": 0, "sun": 0}

for rivi in tiedosto:
    if rivinumero > 1:
        viikonpäivä = rivi[8:11]
        viikonpäivät[viikonpäivä] += 1

    rivinumero += 1

tiedosto.close()

#Tulosten näyttäminen
print(f"Tulokset {rivinumero} rivin käsittelyn jälkeen:")
print(f"Mon: {viikonpäivät['mon']}")
print(f"Tue: {viikonpäivät['tue']}")
print(f"Wed: {viikonpäivät['wed']}")
print(f"Thu: {viikonpäivät['thu']}")
print(f"Fri: {viikonpäivät['fri']}")
print(f"Sat: {viikonpäivät['sat']}")
print(f"Sun: {viikonpäivät['sun']}")