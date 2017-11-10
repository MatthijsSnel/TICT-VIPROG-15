bruin = {'Boxtel', 'Best', 'Eindhoven', "Helmond 't Hout", 'Helmond', 'Helond Brouwhuis', 'Deurne'}
groen = {'Boxtel', 'Best', 'Eindhoven', 'Geldrop', 'Heeze', 'Weert'}

print('Beide trajecten doen de volgende stations aan: {}'.format(bruin.intersection(groen)))
print('Traject bruin doet als enige deze stations aan: {}'.format(bruin.difference(groen)))
print('Alle stations op beide trajecten: {}'.format(bruin.union(groen)))
