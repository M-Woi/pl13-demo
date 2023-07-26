def sum_of_positive_numbers(numbers):
    positive_numbers = []
    for i in numbers:
        if i > 0:
            positive_numbers.append(i)
    return sum(positive_numbers)
