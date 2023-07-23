foo1 = 1  # int
foo2 = 1.2  # float
foo3 = 'bar'  # str
foo4 = False  # bool
foo5 = None  # None
foo6 = [1, 2, 3]  # list
foo7 = (1, 2, 3)  # tuple
foo8 = {1, 2, 3}  # set
foo9 = {'spam': 1, 'eggs': 2}  # dict

foo = [foo1, foo2, foo3, foo4, foo5, foo6, foo7, foo8, foo9]

print(type(foo1))
print(type(foo2))
print(type(foo3))
print(type(foo4))
print(type(foo5))
print(type(foo6))
print(type(foo7))
print(type(foo8))
print(type(foo9))

print("teraz lista")

for item in foo:
    print('take1', type(item))


# Using a loop to iterate through the range of indices of the list foo
for i in range(len(foo)):
    print('take2', type(foo[i]))