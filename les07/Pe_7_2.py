while True:
    woord = input('Geef een string van vier letters: ')
    if len(woord) != 4:
        print('{} heeft {} lengte'.format(woord, str(len(woord))))
    else:
        print('{} heeft een goede lengte'.format(woord))
        break