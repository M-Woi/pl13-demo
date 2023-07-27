slownik_pokazowy = {
    'key1': 'value',
    'key2': 2,
    'key3': (1, 2, 3, 4),
    'key4': ['v', 'a', 'lue'],
    'key5': {'key1': 'value'},  # bez ,
}

'key1' in slownik_pokazowy.keys()

slownik_pok_values = list(slownik_pokazowy.values())
slownik_pokazowy.items()
list(slownik_pokazowy.items())[3]

'value' in slownik_pokazowy.values()
list(slownik_pokazowy.values()).index(2)
list(slownik_pokazowy.items())[1]


for key in slownik_pokazowy:
    if True:
        print(key)

for i in range(10):
    if i % 3 == 0:
        continue
    print(i)
        

