print ("hello, World!")
print ("tyst Fayaz, kram")
print ("hej, mitt namn är Viktoria")
print ("wow!")

name = "Viktoria"
age = 29
print (f"Welcome, {name}! You are {age} years old.")


x = 10
y = 20
z = (x + y)
print (f"Summan av x och y är: {z}")

heltal = 10
flyttal = 3.14
text = "Python är roligt"
sanningsvärde = True

print(type(heltal))
print(type(flyttal))
print(type(text))
print(type(sanningsvärde))

x = 42
y = str(x)
print (y)
print (type(y))

x = "123"
y = 2
z = int(x)
print (z * y)

#+, -, *, /, //, %, **
x = 10
y = 3
print (x + y)
print (x - y)
print (x * y)
print (x / y)
print (x // y)
print (x % y)
print (x ** y)

pi = 3.14
x = int(pi)
print (y)

heltal = 5
y = float(heltal)
print (y)

resultat = round(0.1 + 0.2, 2)
print (resultat)

from decimal import Decimal
x = Decimal("0.1")
y = Decimal("0.2")
resultat = x + y 
print (resultat)

x = input ("ange ett tal: ")
y = input ("ange ett tal: ")
summa = int(x) + int(y)
print (f"summan är: {summa}")

x = input ("vad heter du? ")
y = input ("Glöm inte ditt efternamn! ")
svar = str(x) + " " + str(y)
print (f"Välkommen! {svar}")

x = 42
text = "talet är: " + str(x)
print (text)

text = "Data Science"
print (text[0])
print (text[-1])
print (text[:6])

text = "Python är Kul!"
print (text.upper())
print (text.strip())
print (text.replace("Kul", "fantastisk"))

namn = input ("Vad heter du?: ")
ålder = input ("Hur gammal är du?: ")
print (f"Hej, {namn}! Du är {ålder} år gammal")

try:
    x = int("hej")
except:
    print("Ett fel uppstod")


reallyLongList = ["äpple", "banan", "körsbär", "druva", "apelsin", "päron", "kiwi", "mango", "passionsfrukt", "ananas"]

for i, fruit in enumerate(reallyLongList):
    if i == (i+1):
        continue
    if (i+1) % 3 == 0:
        print(fruit)

