
# Skapa en lista med 5 städer
cities = ["NewYork", "Stockholm", "Sydney", "London", "Dakar"]
print (cities)

#Lägg till ny stad i slutet av listan
cities.append("Oslo")
print (cities)

#Ta bort den andra staden i listan
cities.remove("Stockholm")
print(cities)

#Skriv ut alla städer med en for-loop
for index, cities in enumerate(cities, start = 1):
    print(f"{index}. {cities}")

#Skapa en lista med 5 heltal
heltal = [1, 2, 3, 4, 5]
print(heltal)

#Summera alla tal i listan
summa = sum(heltal)
print(summa)

#Skapa en lista med namn och sök efter ett namn med en for-loop
namnLista = ["Anna", "Peter", "Saga", "Elsa", "Martin"]
print(namnLista[2])