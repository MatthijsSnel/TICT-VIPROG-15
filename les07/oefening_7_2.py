week = {'ma': 'maandag', 'di':'dinsdag','wo': 'woensdag', 'do':'donderdag', 'vr':'vrijdag' }
print(week)
print(week['ma'])
week['za'] = 'zaterdag'
print(week)

for afkorting in week.keys():
    print(afkorting)
for langenaam in week.values():
    print(langenaam)

for beide in week.items():
    print (beide)

for afkorting in week.keys():
    print(afkorting, week[afkorting])

for afkorting in week:
    print('afkorting: {}, lange naam: {}' .format(afkorting, week[afkorting]))
