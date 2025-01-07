
import random

print("Hej och välkommen till 'Sten, sax, påse'")

while True:
    x = input ("Välj mellan sten, sax, påse" + " ")

    if x == "avsluta":
        print("Tack för att du spelade")
        break

    if x not in ["sten", "sax", "påse"]:
        print("Ogiligt")
    
    val = random.choice(["Sten", "sax", "påse"])

    if x == val:
        print("Det blev oavgjort, testa igen!")

    elif (x == "sten" and val == "sax") or (x == "påse" and val == "sten") or (x == "sax" and val == "påse"):
        print("Grattis du vann!")

    else: 
        (x == "påse" and val == "sax") or (x == "sax" and val == "sten") or (x == "sten" and val == "påse")
        print("Tyvärr, du förlorade!")