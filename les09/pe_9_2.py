import csv

with open('inloggers.csv','w', newline='')as myCSVFile:
    writer = csv.writer(myCSVFile, delimiter= ';')
    while True:
        naam = input('Wat is je naam? ')
        if naam == 'einde':
            break
        voorl = input('wat zijn je voorletters? ')
        gebdatum = input('wat is je geboortedatum? ')
        email = input('wat is e-mailadres? ')
        writer.writerow(naam,voorl,gebdatum,email)
