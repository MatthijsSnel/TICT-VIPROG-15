tabel = [[4, 7, 2, 5],[5,1,9,2],[8,3,6,6]]

for rij in range (3):
    for kolom in range(4):
     print(tabel[rij][kolom], end = '')
    print()

tabel = [[4, 7, 2, 5],[5,1,9,2],[8,3,6,6]]

for rij in range(len(tabel)):
    for kolom in range(len(tabel[0])):
     print(tabel[rij][kolom], end = '')
    print()

aatalrijen = len(tabel)
aantalkolommen = len(tabel[0])
for rij in range(aatalrijen):
    for kolom in range(aantalkolommen):
        print (tabel[rij][kolom], end = ' ')
    print()
