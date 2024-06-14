'''Порахувати кількість унікальних символів в строці.
Якщо їх більше 10 - вивести в консоль True, інакше - False.
Строку отримати за допомогою функції input()'''

# snt = 'The weather is fine'
snt = input()

# шукаємо кількість унікальних символів в строці
counter = {}

for char in snt:
    counter[char] = counter.get(char, 0) + 1

print(counter)

# перевіряємо чи кількість унікальних символів > 10
count = 0

for value in counter.values():
    if value == 1:
        count += 1

if count > 10:
    print('true')
else:
    print('false')
