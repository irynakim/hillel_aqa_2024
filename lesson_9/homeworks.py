# lesson7 task 2
"""  Написати функцію, яка обчислює суму двох чисел.
"""


def add_numbers(a, b):
    sum = a + b
    return sum


# print("Sum of two numbers is", add_numbers(40, 2))

# lesson7  task 3
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""


def average(numbers):
    sum_num = 0
    for num in numbers:
        sum_num = sum_num + num
    avg = sum_num / len(numbers)
    return avg


# print("The average is", average([1, 2, 3, 4, 5, 6]))

# lesson7 task 8
'''6.4 - Є ліст з числами, порахуйте сумму усіх ПАРНИХ чисел в цьому лісті'''


def sum_numbers(lst):
    sum_of_even_numbers = 0
    for s in lst:
        if type(s) is int and s % 2 == 0:
            sum_of_even_numbers += s
    return sum_of_even_numbers

# print('Сума усіх парних чисел в лісті = ', sum_numbers([7, 5, 3, 2, 4, 6, 90, 8, 54, 35, 68, 65, 43, 33, 55]))
