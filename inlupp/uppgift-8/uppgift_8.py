# Uppgift 8
# Skapa en funktion count_letters(string) som returnerar en dictionary med varje bokstav som nyckel och antalet förekomster som värde.

def count_letters(string):
    letter_counts = {}  
    for char in string:
            if char in letter_counts:  
                letter_counts[char] += 1  
            else:
                letter_counts[char] = 1  
    return letter_counts  

print(count_letters("hello")) #output {'h': 1, 'e': 1, 'l': 2, 'o': 1}
print(count_letters("")) #output {}
print(count_letters("aaa")) #output {'a': 3}