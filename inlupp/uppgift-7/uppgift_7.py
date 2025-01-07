# Uppgift 7
# Skapa en funktion validate_password(password) som kontrollerar att lösenordet är minst 8 tecken långt och innehåller minst en siffra.

def validate_password(password):
    """
    Skriv beskrivning här.
    """
    if len(password) < 8:
        return False

    elif not any (char.isdigit() for char in password):
        return False
    
    return True

print(validate_password("abc12345"))
print(validate_password("short"))
print(validate_password("password1"))
