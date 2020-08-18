import sqlite3

print("Aloitetaan suoritus")
conn = sqlite3.connect('henkilöt.db')
print("Tietokanta avattu")

# vaihe 1, tietokannan rakenteen luonti
sql = """CREATE TABLE IF NOT EXISTS nimet (
    nimi text,
    ikä integer)"""

print("Lisätään taulu tietokantaan")
kursori = conn.cursor()
kursori.execute(sql)
print("Lisätty taulu tietokantaan")

# vaihe 2, lisätään rivi kantaan
nimi = input("Anna henkilön nimi: ")
ikä = input("Anna henkilön ikä: ")

sql = f'INSERT INTO nimet VALUES ("{nimi}", {ikä})'
kursori.execute(sql)
conn.commit()
print("tallennus tehty")

# vaihe 3, tulostetaan rivit kannasta
print()
print("Tietokannan sisältö:")
sql = "SELECT nimi, ikä FROM nimet"
for rivi in kursori.execute(sql):
    print(rivi)


# suljetaan tietokantayhteys
conn.close()
print()
print("Tietokantayhteys suljettu")