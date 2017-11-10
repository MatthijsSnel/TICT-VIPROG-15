namendict = {}
naam = input('volgende naam')
while naam != '':
    if naam in namendict:
        namendict[naam] += 1
        
    else:
        namendict[naam] = 1

