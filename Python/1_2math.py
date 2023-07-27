# Zadanie 2
print("\nZadanie 2:")
try:
    num1 = float(input("Podaj pierwszą liczbę: "))
    num2 = float(input("Podaj drugą liczbę: "))

    print(f'{num1} + {num2} = {num1 + num2}')
    print(f'{num1} - {num2} = {num1 - num2}')
    print(f'{num1} * {num2} = {num1 * num2}')
    print(f'{num1} / {num2} = {num1 / num2}')
    print(f'{num1} // {num2} = {num1 // num2}')
    print(f'{num1} % {num2} = {num1 % num2}')
    print(f'{num1} ** {num2} = {num1 ** num2}')
except ValueError:
    print("Błąd! Podane wartości nie są liczbami.")