tempratuur = eval(input('welke temperatuur is het vandaag is? '))
    if tempratuur <= 0:
        print('het vriest' )
    elif tempratuur >= 0 and tempratuur <= 15:
        print('het is koud')
    else:
        print('het is lekker weer')


def functie(tempratuur):

    if tempratuur <= 0:
        print('het vriest')
    elif tempratuur >= 0 and tempratuur <= 15:
        print('het is koud')
    else:
        print('het is lekker weer')

tempratuur = eval(input('welke temperatuur is het vandaag is? '))


functie(tempratuur)


