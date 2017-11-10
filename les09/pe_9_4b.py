import csv

with open('producten.csv','r')as myCSVFile:
    reader = csv.DictReader(myCSVFile, delimiter = ';')
    maxprijs = 0
    for row in reader:
        print = int(row['prijs'])
    if prijs > maxprijs:
        maxprijs = maxprijs
        maxnaam = row['naam']


