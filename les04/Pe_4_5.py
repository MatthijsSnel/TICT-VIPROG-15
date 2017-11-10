def kwadraten_som(grondgetallen):
    som = 0
    for getal in grondgetallen:
        if getal > 0:
            som += getal**2
    return som



grondgetallen = [8, 5, 9, -3]
print(kwadraten_som(grondgetallen))