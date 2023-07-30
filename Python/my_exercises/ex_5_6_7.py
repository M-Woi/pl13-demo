# zadanie 5 Define a function to check if a word is a palindrome
def is_palindrome(word):
    # Convert the word to lowercase to ignore case sensitivity
    word = word.lower()

    # Remove any non-alphanumeric characters from the word using a list comprehension
    cleaned_word = ''.join(char for char in word if char.isalnum())

    # Compare the cleaned word with its reverse to check if it's a palindrome
    if cleaned_word == cleaned_word[::-1]:
        return True
    else:
        return False


# Get user input for the word to be checked
word_to_check = input("Enter a word: ")

# Check if the word is a palindrome and print the result
if is_palindrome(word_to_check):
    print("It's a palindrome!")
else:
    print("It's not a palindrome.")

# zadanie 6
def czy_pierwsza(n):
    # Check if the number is equal to 2, as 2 is the only even prime number
    if n == 2:
        return True
    # Check if the number is even or less than or equal to 1, both of which are not prime numbers
    if n % 2 == 0 or n <= 1:
        return False

    # Calculate the square root of the number and add 1 to the result
    # The +1 is needed because range() does not include the stop value
    pierw = int(n**0.5) + 1

    # Iterate through odd numbers starting from 3 up to pierw (exclusive)
    # We use a step size of 2 to only check odd numbers (since even numbers other than 2 are not prime)
    for dzielnik in range(3, pierw, 2):
        # Check if the number is divisible by any of the odd numbers in the range
        if n % dzielnik == 0:
            return False
    # If the number is not divisible by any of the odd numbers in the range, it's prime
    return True

# zadanie 7
# Get the lower and upper bounds of the range from the user
lower_bound = int(input("Enter the lower bound of the range: "))
upper_bound = int(input("Enter the upper bound of the range: "))

# Loop through each number in the range
for liczba in range(lower_bound, upper_bound + 1):
    # Check if the number is divisible by 3
    if liczba % 3 == 0:
        # If it is divisible by 3, print the message
        print(f'{liczba} is divisible by 3')

    # Calculate the integer part of division by 3 for numbers divisible by 2
    if liczba % 2 == 0:
        calkowita_czesc = liczba // 3
        # Print the calculated integer part
        print(f'Integer part of {liczba} divided by 3 is: {calkowita_czesc}')

    # Calculate the remainder of division by 7 for numbers not divisible by 2 and 3
    if liczba % 2 != 0 and liczba % 3 != 0:
        reszta = liczba % 7
        # Print the calculated remainder
        print(f'Remainder of {liczba} divided by 7 is: {reszta}')