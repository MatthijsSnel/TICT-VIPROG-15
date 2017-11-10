with open('kluizen.txt', 'r') as f:
    inlog = [x.strip().split(':') for x in f.readlines()]
    def  toon_aantal_kluizen_vrij(): #maak een list met alle kluisnummers
        aantalBezet = 0
        maxKluis = 12
        mogelijk = ['1','2','3','4','5','6','7','8','9','10','11','12']
        for combi in inlog:
            if combi[0] in mogelijk:
                mogelijk.remove(combi[0])
                aantalBezet += 1
        beschikbaar = maxKluis - aantalBezet
        if beschikbaar > 1:
            print('Er zijn {} kluizen beschikbaar.'.format(beschikbaar))
        elif beschikbaar == 1:
            print('Er is {} kluis beschikbaar.'.format(beschikbaar))
        elif beschikbaar == 0:
            print('Er zijn geen kluizen beschikbaar.')

    def kluis_openen():
        stringnummer = eval(input('wat is je nummer: '))
        code = input('wat is je code: ')
        gegegevenscorrect = False
        stringkluisnummer = inlog[stringnummer][0]
        print(inlog[stringnummer][0])
        stringkluisww = inlog[stringnummer-1][1]
        if stringnummer == stringkluisnummer and code == stringkluisww:
            print('de kluis wordt geopend')
        else:
            print('de kluis wordt niet geopend')



    #def nieuwe_kluis():
    #    lst = [1,2,3,4,5,6,7,8,9,10,11,12]
    #    infile = open('kluizen.txt')
    #    inhoud = infile.readlines()







    print('1: Ik wil weten hoeveel kluizen nog vrij zijn\n'
    '2: Ik wil een nieuwe kluis\n'
    '3: kluis openen\n'
    '4: Ik geef mijn kluis terug\n')

    keuze = int(input('geef de menukeuze: '))

    if keuze == 1:
        toon_aantal_kluizen_vrij()
    elif keuze == 2:
        nieuwe_kluis()
    elif keuze == 3:
        kluis_openen()
    elif keuze == 4:
        kluis_teruggeven()
    else: print('ongeldig')


