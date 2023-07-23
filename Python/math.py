import random

komputer_wybor = random.randint(0, 2)  # random.randint(1, 100)
czlowiek_wybor = input("Wybierz liczbę\n")

print('Wybór komputera: ', komputer_wybor)

if int(komputer_wybor) == int(czlowiek_wybor):
    print('dobrze')
elif int(czlowiek_wybor) > int(komputer_wybor):
    print('Za duzo')
elif int(czlowiek_wybor) < int(komputer_wybor):
    print('Za malo')

    """
    komputer_wybor = random.randint(1, 100)
    czlowiek_wybor = input("Wybierz liczbę\n")

    print('Wybór komputera: ', komputer_wybor)

    if not komputer_wybor == czlowiek_wybor:
        print('zle')
    """