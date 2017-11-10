import csv

with open('producten.csv','w', newline='') as myCSVFile:
    writer = csv.writer(myCSVFile, delimiter=';')
    writer.writerow(('artikelnummer','artikelcode','Naam','Voorraad','Prijs'))
    while True:
        artikelnummer = input('geef je code: ')
        if artikelnummer == '':
            break
        artikelcode = input('geef de code aan: ')
        naam = input('geef de naam van de artikel aan: ')
        vooraad = input('geef de aantal van de vooraad aan: ')
        prijs = input('geef de prijs aan: ')
        writer.writerow((artikelnummer,artikelcode,naam,vooraad,prijs))
