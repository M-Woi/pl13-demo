# Zadanie 3
print("\nZadanie 3:")
x_coords = input("Podaj współrzędne x oddzielone spacją: ").split()
y_coords = input("Podaj współrzędne y oddzielone spacją: ").split()

x_coords = list(map(float, x_coords))
y_coords = list(map(float, y_coords))

# Wypisanie współrzędnych punktów
print("Współrzędne punktów:")
for x, y in zip(x_coords, y_coords):
    print(f'({x}, {y})')

# Punkt najbardziej oddalony od osi X i osi Y
max_x = max(x_coords)
max_y = max(y_coords)
print(f'Punkt najbardziej oddalony od osi X: ({max_x}, 0)')
print(f'Punkt najbardziej oddalony od osi Y: (0, {max_y})')