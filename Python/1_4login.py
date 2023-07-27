# Zadanie 4
print("\nZadanie 4:")
users = {
    'user1': {
        'imie': 'Jan',
        'nazwisko': 'Kowalski',
        'email': 'jan.kowalski@example.com'
    },
    'user2': {
        'imie': 'Anna',
        'nazwisko': 'Nowak',
        'email': 'anna.nowak@example.com'
    },
    'user3': {
        'imie': 'Tomasz',
        'nazwisko': 'Mazur',
        'email': 'tomasz.mazur@example.com'
    }
}

login = input("Podaj login użytkownika: ")

if login in users:
    user_data = users[login]
    print(f"Dane użytkownika o loginie '{login}':")
    print(f"Imię: {user_data['imie']}")
    print(f"Nazwisko: {user_data['nazwisko']}")
    print(f"Email: {user_data['email']}")
else:
    print(f"Użytkownik o loginie '{login}' nie istnieje.")
