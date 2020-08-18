tiedosto = open("forestfires.csv", "r")

rivinumero = 1

lukumäärä_mon = 0
lukumäärä_tue = 0
lukumäärä_wed = 0
lukumäärä_thu = 0
lukumäärä_fri = 0
lukumäärä_sat = 0
lukumäärä_sun = 0

for rivi in tiedosto:
    if rivinumero > 1:
        viikonpäivä = rivi[8:11]
        if viikonpäivä == "mon":
            lukumäärä_mon += 1
        elif viikonpäivä == "tue":
            lukumäärä_tue += 1
        elif viikonpäivä == "wed":
            lukumäärä_wed += 1
        elif viikonpäivä == "thu":
            lukumäärä_thu += 1
        elif viikonpäivä == "fri":
            lukumäärä_fri += 1
        elif viikonpäivä == "sat":
            lukumäärä_sat += 1
        elif viikonpäivä == "sun":
            lukumäärä_sun += 1
        else:
            print("Tuntematon viikonpäivä: " +viikonpäivä)
    rivinumero += 1

tiedosto.close()

#Tulosten näyttäminen
print(f"Mon: {lukumäärä_mon}")
print(f"Tue: {lukumäärä_tue}")
print(f"Web: {lukumäärä_wed}")
print(f"Thu: {lukumäärä_thu}")
print(f"Fri: {lukumäärä_fri}")
print(f"Sat: {lukumäärä_sat}")
print(f"Sun: {lukumäärä_sun}")