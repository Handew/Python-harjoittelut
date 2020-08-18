import http.client

conn = http.client.HTTPSConnection("www.ilmatieteenlaitos.fi")
conn.request("GET", "/saa/porvoo")
vastaus = conn.getresponse()
html = str(vastaus.read())

# print(html[:500])
indeksi = html.index('<div class="temperature positive')
alku = indeksi+78
loppu = alku+2
lämpötila = html[alku:loppu]
print(f"Lämpötila Porvoossa: {lämpötila} astetta.")