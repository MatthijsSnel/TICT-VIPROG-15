studentencijfers = [ [95, 92, 86],[66, 75, 54],[89, 72, 100],[34, 0, 0] ]
gemiddelden = []
totaal = 0
aantal = 0
totGemiddeld = 0
def gemiddelde_per_student(studentencijfers):
   for lijst in studentencijfers:
       aantal = 0
       totaal = 0
       for cijfer in lijst:
           aantal += 1
           totaal += cijfer
       gemiddelden.append(totaal/aantal)
   return gemiddelden
def gemiddelde_van_alle_studenten(studentencijfers):
   aantal = 0
   totaal = 0
   for i in gemiddelde_per_student(studentencijfers):
       aantal += 1
       totaal += i
   antw = (totaal/aantal)
   return antw

print(gemiddelde_per_student(studentencijfers))
print(gemiddelde_van_alle_studenten(studentencijfers))