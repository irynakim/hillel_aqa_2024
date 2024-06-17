print('task1----------------------------------------------')
# task 1
""" Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та випраавити\доповнити.
"""


# def multiplication_table(number):
#     multiplier = 1
#     while multiplier <= 9:
#         result = number * multiplier
#         if result < 25:
#             print(str(number) + "x" + str(multiplier) + "=" + str(result))
#         multiplier += 1
# multiplication_table(3)
#
# print('----------------------')
def multiplication_table(number):
    multiplier = 1
    result = 0
    while result <= 25:
        print(str(number) + "x" + str(multiplier) + "=" + str(result))
        result = number * multiplier
        multiplier += 1
multiplication_table(3)

print('\ntask2----------------------------------------------')
# task 2
"""  Написати функцію, яка обчислює суму двох чисел.
"""


def add_numbers(a, b):
    sum = a + b
    return sum


print("Sum of two numbers is", add_numbers(40, 2))

print('\ntask3----------------------------------------------')
# task 3
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""


def average(numbers):
    sum_num = 0
    for num in numbers:
        sum_num = sum_num + num
    avg = sum_num / len(numbers)
    return avg


print("The average is", average([1, 2, 3, 4, 5, 6]))

print('\ntask4----------------------------------------------')
# task 4
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""


def reverse_string(string):
    reversed_string = ""
    for char in string:
        reversed_string = char + reversed_string
    return reversed_string


print("Reversed String:", reverse_string('String'))

print('\ntask5----------------------------------------------')
# task 5
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""


def string(string):
    max_length = 0
    for word in string:
        length = len(word)
        if length > max_length:
            max_length = length
            max_word = word
    return max_word


print("Max word:", string(['test', 'quazar', 'qwerty', 'row']))

print('\ntask6----------------------------------------------')
# task 6
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""


def find_substring(sub, s):
    index_s = 0
    while (index_s < len(s)):
        f_is = True
        index_sub = 0
        while index_sub < len(sub):
            if (index_s + index_sub) == len(s):
                f_is = False
                index_s = len(s) - 1
                break
            if s[index_s + index_sub] != sub[index_sub]:
                f_is = False
                break
            else:
                index_sub = index_sub + 1
        if f_is:
            return index_s
        else:
            index_s = index_s + 1
    return -1


str1 = "Hello, world!"
str2 = "world"
print(find_substring(str2, str1))  # поверне 7

str1 = "The quick brown fox jumps over the lazy dog"
str2 = "cat"
print(find_substring(str2, str1))  # поверне -1

print('\ntask7----------------------------------------------')
# task 7
'''6.3 - Є list з даними lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum'].
Напишіть код, який свормує новий list (наприклад lst2),
який містить лише змінні типу стрінг, які присутні в lst1. Данні в лісті можуть бути будь якими'''


def data_list(lst1):
    lst2 = []
    for s in lst1:
        if type(s) is str:
            lst2.append(s)
    return lst2


print(data_list(['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']))

print('\ntask8----------------------------------------------')
# task 8
'''6.4 - Є ліст з числами, порахуйте сумму усіх ПАРНИХ чисел в цьому лісті'''


def sum_numbers(lst):
    sum_of_even_numbers = 0
    for s in lst:
        if type(s) is int and s % 2 == 0:
            sum_of_even_numbers += s
    return sum_of_even_numbers


print('Сума усіх парних чисел в лісті = ', sum_numbers([7, 5, 3, 2, 4, 6, 90, 8, 54, 35, 68, 65, 43, 33, 55]))

print('\ntask9----------------------------------------------')
# task 9
"""3.7
Знайди остачу від діленя чисел:
a) 8019 : 8     d) 7248 : 6
b) 9907 : 9     e) 7128 : 5
c) 2789 : 5     f) 19224 : 9
"""


def restant(a, b):
    result = a % b
    return result


print(restant(8019, 8))
print(restant(9907, 9))
print(restant(2789, 5))
print(restant(7248, 6))
print(restant(7128, 5))
print(restant(19224, 9))

print('\ntask10----------------------------------------------')
# task 10
""" 4.3 - Зробіть так, щоб у тексті було не більше одного пробілу між словами.
"""


def spaces(text):
    text = text.split()
    text = ' '.join(text)
    return text


print(spaces('       aahh   swded      dede        f      '))

"""  Оберіть будь-які 4 таски з попередніх домашніх робіт та
перетворіть їх у 4 функції, що отримують значення та повертають результат.
Обоязково документуйте функції та дайте зрозумілі імена змінним.
"""
