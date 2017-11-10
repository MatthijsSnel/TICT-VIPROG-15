stations = ['Schagen', 'Heerhugowaard', 'Alkmaar', 'Castricum', 'Zaandam', 'Amsterdam Sloterdijk', 'Amsterdam Centraal', 'Amsterdam Amstel', 'Utrecht Centraal', 's-Hertogenbosch', 'Eindhoven', 'Weert', 'Roermond', 'Sittard', 'Maastricht']

def inlezen_beginstation():
    beginstation = ""
    while beginstation not in stations:
        beginstation = input('geef beginstation: ')
    return beginstation

beginstation = inlezen_beginstation()

def inlezen_eindstation():
    eindstation = ""
    while eindstation not in stations:
        eindstation = input('geef eindstation: ')
    return eindstation

eindstation = inlezen_eindstation()

def omroepen_reis(beginstation, eindstation):
    nummerB = stations.index(beginstation) + 1
    nummerE = stations.index(eindstation) + 1
    verschil = nummerE - nummerB
    prijs = verschil * 5

    if verschil < 0:
        eindstation=stations[-1]
        print("Je kan niet terug")
        nummerE = stations.index(eindstation)+1
        verschil = nummerE - nummerB




    print('het beginstation is {} en is het {}e station in het traject' .format(beginstation, nummerB))
    print('het eindstation is {} en is het {}e station in het traject' .format(eindstation, nummerE))
    print('de afstand is {} stations'.format(verschil))
    print('de prijs van de reis is {} euro' .format(prijs))
    print('het beginstation is {} de stations die worden gepasseerd zijn '.format(beginstation))

    for station in stations[nummerB:nummerE-1]:
        print('-'+station)
    print('het eindstation is {}'.format(eindstation))




