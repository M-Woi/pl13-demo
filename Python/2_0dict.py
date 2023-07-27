slownik_pokazowy = {
    'key1': 'value',
    'key2': 2,
    'key3': (1, 2, 3, 4),
    'key4': ['v', 'a', 'lue'],
    'key5': {'key1': 'value'},  # bez ,
}

del slownik_pokazowy['key5']  # usuń klucz
slownik_pokazowy['key5'] = {'nowy_key5': 'value'}  # dodaj nowy klucz
print(slownik_pokazowy['key5'])


slownik_pokazowy['calkiem_nowy_klucz'] = 'tatatt'

print(slownik_pokazowy['key2'])
slownik_pokazowy['key2'] = 5
print(slownik_pokazowy['key2'])

print(slownik_pokazowy['key3'])
len(slownik_pokazowy['key3'])
print(slownik_pokazowy['key3'])


# niehashowalne nie mogą bybć kluczmi w słowniku


test = slownik_pokazowy['key5']['key1']  # ważne
test2 = slownik_pokazowy['key5']

print.slownik_pokazowy.get([key1])

# extend a dodawanie - nie tworzy

