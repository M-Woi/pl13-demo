def find_max_odd_number(numbers):
    max_odd = None
    for i in numbers:
        if i % 2 == 1:
            if i > max_odd:
                max_odd = i
    return max_odd

