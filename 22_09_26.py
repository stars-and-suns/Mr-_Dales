def create_word(word1:str, word2:str):
    # turning the second word into a list and making a boolean variable
    letters = list(word2)
    can_be_made = True

    # iterating through the first word and checking if it correlates
    # to the letters in word 2
    for letter in word1:
        if letter in letters:
            letters.remove(letter)
        else:
            can_be_made = False

    # checking if the boolean variable is True or False
    if can_be_made == True:
        print(f'The word {word1} CAN be made using the letters in {word2}')

    else:
        print(f'The word {word1} CANNOT be made using the letters in {word2}')

create_word('EAT', 'ATE')
create_word('EAT','HEART')
create_word('MEET','MEAT')

def enter_digits(num:int):
    numbers = []
    highest_frequency = 0
    mode = ''
    repeat = 0

    # getting input for numbers from user and making sure they're only one digit
    print(f'You must enter {num} digits')
    for i in range(num):
        number = input(f'Number {i+1}: ')
        while len(str(number)) > 1 or not number.isdigit():
            number = input(f'Try again: ')
        numbers.append(number)

    # comparing numbers to see which appears most
    for n in numbers:
        if str(numbers).count(str(n)) > highest_frequency:
            highest_frequency = str(numbers).count(str(n))
            mode = str(n)

    # checking how many numbers appear the same number of times as the
    # highest frequency to check if the data is multimodal
    no_repeat_numbers = set(numbers)
    for n in no_repeat_numbers:
        if str(numbers).count(str(n)) == highest_frequency:
            repeat += 1

    # outputting final messages once checking if data has multiple modes
    if repeat > 1:
        print('Data was multimodal')
    else:
        print(f'Most common digit {mode} was entered {highest_frequency} times')

enter_digits(6)

def sequence(end:int):
    largest_chain = 0
    for num in range(1, (end+1)):
        print('num', num)
        new_num = num
        chain = 1
        while new_num > 1:
            if num % 2 == 0:
                new_num = num/2
            else:
                new_num = 3 * num + 1
            chain += 1

        if chain > largest_chain:
            largest_chain = chain

    print(largest_chain)

sequence(10)