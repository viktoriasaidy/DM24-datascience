
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
