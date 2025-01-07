# Uppgift 6
# Skapa en funktion multiplication_table(n, limit) som returnerar multiplikationstabellen för n upp till limit i en lista.

def multiplication_table(n, limit):
    reslutat = []
    for i in range (1, limit + 1):
        reslutat.append(n * i)
    """
    Skriv beskrivning här.
    """
    return reslutat
n = 2
limit = 3
print(multiplication_table(n, limit))




