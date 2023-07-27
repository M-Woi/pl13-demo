print("Zadanie 1:")

try:
    int_to_bool = bool(0)  # int_to_bool
    print(f'bool(0) = {int_to_bool}')
except ValueError as e:
    print(f'int_to_bool -> {e}')



try:
    str_to_int = int('Ala')  # str_to_int
    print(f'int("Ala") = {str_to_int}')
except ValueError as e:
    print(f'int("Ala") -> {e}')



try:
    bool_to_int = int(False)   # bool_to_int
    print(f'int(False) = {bool_to_int}')
except ValueError as e:
    print(f'bool_to_int -> {e}')



try:
    bool_to_int = int(False)   # bool_to_int
    print(f'int(False) = {bool_to_int}')
except ValueError as e:
    print(f'bool_to_int -> {e}')