class OmaLuokka:
    oma_arvo = 100

    def testi(self):
        print("OmaLuokka.testi -metodissa...")

class Auto:
    huippunopeus = 0

# Periminen tapahtuu suluilla
class UrheiluAuto(Auto):
    pass



print("Suoritus alkaa")

instanssi = OmaLuokka()
instanssi.testi()

print(instanssi.oma_arvo)
instanssi.oma_arvo = 200
print(instanssi.oma_arvo)


print("Suoritus päättyy")
