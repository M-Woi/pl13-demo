for i in range(-1, 13):
    if i % 3 == 0:
        continue

    if i > 10:
        print('stop wiecej niz 10')
        break
    print(i)
else:
    print('koniec')

def count_down(number):
    while number:
        print(number)
        number -= 1
    print('lift off')
count_down(10)  # no indentation

# Dane wejściowe - dwie listy numeryczne, jedna odpowiada za współrzędną x, druga za y.
x = [1, 4, 8, 93, 1.5, 7.6, 90]
y = [67, 32, 2, 79, 45, 53, 3]

# Używamy list(zip()) do połączenia współrzędnych x i y w pary punktów (x, y).
points = list(zip(x, y))

# a) Znalezienie najbliższego i najdalszego punktu względem punktu (0,0).
# Ustawiamy początkowe wartości dla najbliższego i najdalszego punktu na pierwszy punkt.
nearest_point = points[0]
farthest_point = points[0]
# Ustawiamy początkową minimalną i maksymalną odległość na odległość od pierwszego punktu do (0,0).
min_distance = nearest_point[0]**2 + nearest_point[1]**2
max_distance = min_distance

# Iteracja przez pozostałe punkty, aby znaleźć najbliższy i najdalszy punkt.
for point in points[1:]:
    # Obliczenie odległości od (0,0) dla bieżącego punktu.
    distance = point[0]**2 + point[1]**2
    # Porównanie odległości z minimalną i maksymalną odległością.
    if distance < min_distance:
        min_distance = distance
        nearest_point = point
    if distance > max_distance:
        max_distance = distance
        farthest_point = point

# b) Obliczenie pola prostokąta, którego najbliższy i najdalszy punkt są wierzchołkami.
# Policz różnice między współrzędnymi x i y, aby uzyskać długości boków prostokąta.
width = abs(farthest_point[0] - nearest_point[0])
height = abs(farthest_point[1] - nearest_point[1])
# Obliczenie pola prostokąta jako iloczyn długości boków.
rectangle_area = width * height

# c) Wypisanie punktów wewnątrz prostokąta.
# Utworzenie listy na punkty wewnątrz prostokąta.
points_inside_rectangle = []
# Iteracja przez wszystkie punkty, aby sprawdzić, czy znajdują się wewnątrz prostokąta.
for point in points:
    # Sprawdzenie, czy współrzędne x i y punktu mieszczą się między współrzędnymi najbliższego i najdalszego punktu.
    if nearest_point[0] <= point[0] <= farthest_point[0] and nearest_point[1] <= point[1] <= farthest_point[1]:
        # Jeśli tak, to punkt jest wewnątrz prostokąta i dodajemy go do listy.
        points_inside_rectangle.append(point)

# Wyświetlenie wyników.
print(f"Najbliższy punkt do (0,0): {nearest_point}")
print(f"Najdalszy punkt od (0,0): {farthest_point}")
print(f"Pole prostokąta: {rectangle_area}")
print(f"Punkty wewnątrz prostokąta: {points_inside_rectangle}")