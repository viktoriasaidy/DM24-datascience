
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

print(sum(heltal))

#Skapa en lista med namn och sök efter ett namn med en for-loop
nameList = ["Anna", "Peter", "Saga", "Elsa", "Martin"]
for name in nameList:
    if name == "Peter":
        print("Name found" + " " + name)

#Skapa en dictionary för en produkt
product = {
    "name": "Laptop",
    "price": 1000,
    "inStock": 50
}
print(product)

#1. Skriv ut produktens pris
print(product["price"])

#2. Lägg till en nyckel för "kategori"
product["category"] = "computers"
print(product)

#3. Ändra värdet på "lager" till 40
product["inStock"] = 40
print(product)

#Skapa en dictionary med tre nyckel-värde-par (e.g., "namn", "ålder", "stad")
person = {
    "name": "Viktoria",
    "age": 29,
    "city": "Stockholm"
}
print(person)

# Iterera genom dictionaryn och skriv ut varje nyckel och värde
for key in person:
    print(key)

for value in person.values():
    print(value)

for key, value in person.items():
    print(f"Persons {key}: is {value}")


#Skriv en while-loop som frågar användaren om ett lösenord tills rätt lösenord anges
password = ""
while password != "hejdå":
    password = input("ange lösenord ")
    print ("Fel lösenord, försök igen")
    if password == "hejdå":
        print("Du loggas in")
