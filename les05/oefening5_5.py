infile = open('voorbeeld5_5.txt', 'r')
inhoud = infile.read()
infile.close()
print(inhoud)

infile = open('voorbeeld5_5.txt', 'r') # oefening 5.5b
inhoud1 = infile.read()
infile.close()
inhoud2 = inhoud1.split()
print(inhoud2)

infile = open('voorbeeld5_5.txt', 'r') # oefening 5.5c
inhoud3 = infile.readlines()
infile.close()
print(inhoud3)