# Uppgift 5
# Skapa en funktion filter_odd(numbers) som returnerar en lista med alla jämna tal från den givna listan.

def filter_odd(numbers):
    return [numbers for numbers in numbers if numbers % 2 == 0] 
    """
    Skriv beskrivning här.
    """
numbers = [1, 2, 3, 4]
print(filter_odd(numbers)) 