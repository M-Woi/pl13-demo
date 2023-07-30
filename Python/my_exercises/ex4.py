# Write a function which calculates the average of the numbers in a given list.
# Note: Empty arrays should return 0.
"""
import statistics
numbers = {1, 2, 3, 10}
def find_average(numbers):
    if len(numbers) > 0:
        average = statistics.mean(numbers)
        print(average)
        return statistics.mean(numbers)
    else:
        return 0



Napisz program w którym pobierzesz od użytkownika dwie listy numeryczne,
gdzie jedna odpowiada za współrzędną x a druga za y.

Możesz użyć przykładowych list:
x = [1,4,8,93,1.5,7.6,90]
y = [67,32,2,79,45,53,3]

a) Znajdź 2 punkty: najbliższy i najdalszy względem punktu (0,0).
b) Policz pole prostokąta którego te punkty są wierzchołkami.
c) Wypisz punkty wewnątrz tego prostokąta.

"""
x = eval(input('Podaj wspórzędne X: '))
y = eval(input('Podaj wspórzędne Y: '))
x = [1, 4, 8, 93, 1.5, 7.6, 90]
y = [67, 32, 2, 79, 45, 53, 3]
points = list(zip(x, y))
dist = []
for i in range(len(points)): #  dystans
    dist.append((x[i] ** 2 + y[i] ** 2) ** .5) #  dwie potęgi pod pierwiastkiem

p1 = points[dist.index(min(dist))]
p2 = points[dist.index(max(dist))]
print(f'Punkt 1: {p1}')
print(f'Punkt 2: {p2}')

pole = (p2[0] - p1[0]) * (p2[1] - p1[1])
print('Pole prostokąta opartego na powyższych punktach', pole)

points_inside = []
for i in range(len(points)):
    if x[i] <= p1[0]:
        continue
    if x[i] >= p2[0]:
        continue
    if y[i] <= p1[1]:
        continue
    if y[i] >= p2[1]:
        continue
    points_inside.append(points[i])

print('Punkty wewnątrz prostokąta:', points_inside)