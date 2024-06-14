'''Є ліст з числами, порахуйте сумму усіх ПАРНИХ чисел в цьому лісті'''

lst = [7, 5, 3, 2, 4, 6, 90, 8, 54, 35, 68, 65, 43, 33, 55]

sum_of_even_numbers = 0
for s in lst:
    if type(s) is int and s % 2 == 0:
        sum_of_even_numbers += s
print('Сума усіх парних чисел в лісті = ', sum_of_even_numbers)
