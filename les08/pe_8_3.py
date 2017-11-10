
def code(invoerstring):
    nieuwestring = ''
    for kar in invoerstring:
        nieuweASCII = ord(kar) + 3
        nieuweKAR = chr(nieuweASCII)
        nieuwestring += nieuweKAR
    return nieuwestring



naam = input('geef naam: ')
beginstation = input('geef beginstation: ')
eindstation = input('geef eindstation: ')
invoerstring = naam + beginstation + eindstation

print(code(invoerstring))

