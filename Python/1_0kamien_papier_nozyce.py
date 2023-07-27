import random
computer_wybor = random.wybor(['kamien', 'paper', 'scissor'])
czlowiek_wybor = input("Do you want kamien paper or nozyce?\n")

print('computer_wybor: ', computer_wybor)

if computer_wybor == czlowiek_wybor:
    print('Remis')
elif czlowiek_wybor == 'kamien' and computer_wybor == 'nozyce':
    print('Wygrana')
elif czlowiek_wybor == 'paper' and computer_wybor == 'kamien':
    print('Wygrana')
elif czlowiek_wybor == 'paper' and computer_wybor == 'kamien':
    print('Wygrana')
else:
    print("Przegrywasz")
