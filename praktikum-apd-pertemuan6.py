daftar_buku = {
    "buku1" : "harry potter"
    "buku2" : "pervy jackson"
    "buku3" : "twilight"
}
print(daftar_buku["buku1"])
print(daftar_buku["buku2"])
print(daftar_buku["buku3"])

Biodata = {
    "Nama" : "Aldy Ramadhan Syahputra",
    "NIM" : 2109106079,
    "KRS" : ["Program Web", "Struktur Data", "Basis Data"],
    "Mahasiswa_Aktif" :True,
        "Social Media" : {
        "Instagram" : "@aldyrmdhns_",
        "Discord" : "\'Izanami#6848"
        }
}

games = dict(Sekiro = "Action", Pokemon = "Adventure",
Valorant = {"nama"} : {123 : "informatika"} )
print(games["Pokemon"])

games = {
    "game1" : "pung mobile",
    "game2" : "mobile legend",
    "game3" : {
        "nama" : "coc",
        "genre" : "strategy"
    }

}

print((games.get('game3')).get('nama'))

Nilai = {
    "Matematika" : 80,
    "B. Indonesia" : 90,
    "B. Inggris" : 81,
    "Kimia" : 78,
    "Fisika" : 80
}

#tanpa menggunakan items
for i in Nilai:
    print(i)
    print("")
#menggunakan items
for i, j in Nilai.items():
    print(f"Nilai {i} anda adalah {j}")


Film = {
"Avenger Endgame" : "Action",
"Sherlock Holmes" : "Mystery",
"The Conjuring" : "Horror"
}
#Sebelum Ditambah
print(Film)

Film["Zombieland"] = "Comedy"
Film.update({"Hours" : "Thriller"})
#Setelah Ditambah
print(Film)
#penggunaan del
del Film['Avangers Endgame']
print(Film)
simpan = Film.pop('Hours')
print(Film)
Film["Hours"] = simpan
print(Film)

print("Jumlah Data = ", len(data))

Buku = {
"No Longer Human" : "Osamu Dazai",
"Harry Potter" : "J.K. Rowlings",
"Hamlet" : "William Shakespeare"
}
pinjam = Buku.copy()
print("Dictionary yang Telah Disalin : ", pinjam)

key = "apel", "jeruk", "mangga"
value = 1
buah = dict.fromkeys(key, value)
print(buah)

Nilai = {
"Matematika" : 80,
"B. Indonesia" : 90,
"B. Inggris" : 81,
"Kimia" : 78,
"Fisika" : 80
}
#menggunakan keys
for i in Nilai.keys():
    print(i)
    print("")
#menggunakan value
for i in Nilai.values():
    print(i)

Nilai = {
"Matematika" : 80,
"B. Indonesia" : 90,
"B. Inggris" : 81
}
#sebelum Setdefault
print(Nilai)
print("")
#menggunakan setdefault
print("Nilai : ", Nilai.setdefault("Kimia", 70))
print("")
#setelah menggunakan setdefault
print(Nilai)

Nilai = {
"Matematika" : 80,
"B. Indonesia" : 90,
"B. Inggris" : 81
}
#sebelum Setdefault
print(Nilai)
print("")
#menggunakan setdefault
print("Nilai : ", Nilai.setdefault("Kimia", 70))
print("")
#setelah menggunakan setdefault
print(Nilai)

mahasiswa = {
101 : {"Nama" : "Aldy", "Umur" : 19},
111 : {"Nama" : "Abdul", "Umur" : 18}
}
for key, value in mahasiswa.items():
    print("ID Mahasiswa : ", key)
    for key_a, value_a in value.items():
        print (key_a, " : ", value_a)
print("")

