set1 = {1, 2, 3, 4, (1, 2, 23)}

lst_with_duplicates = [1, 2, 2, 2, 3]
set(lst_with_duplicates)
list(set(lst_with_duplicates))
print(lst_with_duplicates)
print(set1)
len(set1)  #5
# print(sum(set1)) #err

lst_with_duplicates = [1, 2, 2, 2, 3]

# Zamieniamy listę na zbiór, aby pozbyć się duplikatów
unique_set = set(lst_with_duplicates)

# Zamieniamy zbiór na listę, aby uzyskać listę bez duplikatów
unique_list = list(unique_set)

# Wyświetlamy listę bez duplikatów
print(unique_list)
