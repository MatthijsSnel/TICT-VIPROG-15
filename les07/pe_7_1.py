som = 0
aantal = 0
while True:
    getal = eval(input('geef getal'))
    if getal != 0:
        som = som + getal
        aantal = aantal + 1
    else:
        break
    print(aantal, som)

