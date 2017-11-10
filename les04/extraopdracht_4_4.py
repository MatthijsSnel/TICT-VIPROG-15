bedrag = eval(input('wat is uw bedrag op uw rekening? '))
rente = eval(input('wat is uw rente op uw rekening? '))

def eindbedrag(bedrag, percentage):
    nieuwebedrag = (bedrag + rente * bedrag / 100)
    return nieuwebedrag
