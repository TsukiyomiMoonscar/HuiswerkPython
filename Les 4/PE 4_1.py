cijferICOR=(8.5)
cijferPROG=(7)
cijferCSN=(7.5)
gemiddelde=round(((cijferCSN + cijferICOR + cijferPROG)/3),1)
Overzicht=('Het gemiddelde van de drie cursusen is {}\nHet bedrag wat de HU je schenkt is €{},-'.format(gemiddelde, round(gemiddelde*30)))
print(Overzicht)    gdsg