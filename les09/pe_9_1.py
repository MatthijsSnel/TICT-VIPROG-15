try:
    bedrag = 4356
    aantal = eval(input('geef bedrag'))
    if aantal < 0:
        print('negatieve getallen niet teogest')
    else:
        print('bedrag /aantal')
except ZeroDivisionError:
    print('delen door nul kan niet')
except NameError:
    print('gebruiker cijfers')
except:
    print('onjuiste invoer')

