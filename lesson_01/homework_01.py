# task 01 == Виправте синтаксичні помилки
print('task 01------------------------------------------------------')
print("Hello", end=" ")
print("world!")

# task 02 == Виправте синтаксичні помилки
print('\ntask 02----------------------------------------------------')
hello = "Hello"
world = "world"
if True:
    print(f"{hello} {world}!")

# task 03  == Вcтавте пропущену змінну у ф-цію print
print('\ntask 03----------------------------------------------------')
for letter in "Hello world!":
    print(letter)

# task 04 == Зробіть так, щоб кількість бананів була
# завжди в чотири рази більша, ніж яблук
print('\ntask 04----------------------------------------------------')
apples = 2
banana = apples*4
print(banana) #DELETE!!!!!!!!!!!!!!!!!

# task 05 == виправте назви змінних
print('\ntask 05----------------------------------------------------')
storona_1 = 1
storona_2 = 2
storona_3 = 3
storona_4 = 4
print(storona_1, storona_2, storona_3, storona_4) #DELETE!!!!!!!!!!!!!!!!!

# task 06 == Порахуйте периметр фігури з task 05
# та виведіть його для користувача
print('\ntask 06----------------------------------------------------')
perimetery = storona_1 + storona_2 + storona_3 + storona_4
print(perimetery)

"""
    # Задачі 07 -10:
    # Переведіть задачі з книги "Математика, 2 клас"
    # на мову пітон і виведіть відповідь, так, щоб було
    # зрозуміло дитині, що навчається в другому класі
"""
# task 07
"""
У саду посадили 4 яблуні. Груш на 5 більше яблунь, а слив - на 2 менше.
Скільки всього дерев посадили в саду?
"""
print('\ntask 07----------------------------------------------------')
zadacha_07 ="""У саду посадили 4 яблуні. Груш на 5 більше яблунь, а слив - на 2 менше.
Скільки всього дерев посадили в саду?
"""
print(zadacha_07)
print("Розв'язок:")
apple_trees = 4
print('Посадили яблунь:', apple_trees)
pear_trees = apple_trees + 5
print('Посадили груш: яблуні + 5 =', apple_trees, '+ 5 =',  pear_trees)
plum_trees = apple_trees - 2
print('Посадили слив: яблуні - 2 =', apple_trees, '- 2 =', plum_trees)
all_trees = apple_trees + pear_trees + plum_trees
print('Посадили всіх дерев: яблуні + груші + сливи = ', apple_trees, '+', pear_trees, '+', plum_trees, '=', all_trees)
print('Відповідь:', all_trees, 'дерев посадили в саду' )

# task 08
"""
До обіда температура повітря була на 5 градусів вище нуля.
Після обіду температура опустилася на 10 градусів.
Надвечір потепліло на 4 градуси. Яка температура надвечір?
"""
print('\ntask 08----------------------------------------------------')
zadacha_08 ="""До обіда температура повітря була на 5 градусів вище нуля.
Після обіду температура опустилася на 10 градусів.
Надвечір потепліло на 4 градуси. Яка температура надвечір?
"""
print(zadacha_08)
print("Розв'язок задачі:")
temp_do_obidu = 0 + 5
print('Температура повітря до обіду: 0 + 5 = ', temp_do_obidu)
temp_pislja_obidu = temp_do_obidu - 10
print('Температура повітря після обіду: температура повітря до обіду - 10 =', temp_do_obidu, '- 10 = ',  temp_pislja_obidu)
temp_vvecheri = temp_pislja_obidu + 4
print('Температура повітря надвечір: температура повітря після обіду + 4 =', temp_pislja_obidu, '+ 4 =', temp_vvecheri)
print('Відповідь:', temp_vvecheri, 'температура повітря надвечір' )

# task 09
"""
Взагалі у театральному гуртку - 24 хлопчики, а дівчаток - вдвічі менше.
1 хлопчик захворів та 2 дівчинки не прийшли сьогодні.
Скількі сьогодні дітей у театральному гуртку?
"""
print('\ntask 09----------------------------------------------------')
zadacha_09 = """Взагалі у театральному гуртку - 24 хлопчики, а дівчаток - вдвічі менше.
1 хлопчик захворів та 2 дівчинки не прийшли сьогодні.
Скількі сьогодні дітей у театральному гуртку?
"""
print(zadacha_09)
print("Розв'язок задачі:")
boys = 24
print('Всього', boys, ' хлопчики')
girls = boys // 2
print('Всього', girls, ' дівчаток')
print("\nСьогодні 1 хлопчик захворів")
boys_come = boys - 1
print('Прийшло хлопчиків:', boys, '- 1 = ', boys_come)
print("Сьогодні 2 дівчинки не прийшли")
girls_come = girls - 2
print('Прийшло дівчаток: всього дівчаток:', girls, ' - 2 = ', girls_come)
boys_girls_today = boys + girls
print('Сьогодні дітей у театральному гуртку: прийшло хлопчиків + прийшло дівчаток = ', boys_come, '+', girls_come, '=', boys_girls_today)
print('Відповідь:', boys_girls_today, 'сьогодні дітей у театральному гуртку' )

# task 10
"""
Перша книжка коштує 8 грн., друга - на 2 грн. дороже,
а третя - як половина вартості першої та другої разом.
Скільки будуть коштувати усі книги, якщо купити по одному примірнику?
"""
print('\ntask 10----------------------------------------------------')
zadacha_10 = """
Перша книжка коштує 8 грн., друга - на 2 грн. дороже,
а третя - як половина вартості першої та другої разом.
Скільки будуть коштувати усі книги, якщо купити по одному примірнику?
"""
print(zadacha_10)
print("Розв'язок задачі:")
book_1 = 8
print('Перша книжка коштує:', book_1, 'грн.')
book_2 = book_1 + 2
print('Друга книжка коштує: на 2 грн. дороже = ', book_1, ' + 2 =', book_2, 'грн.')
book_3 = (book_1 + book_2) // 2
print('Третя книжка коштує: половина вартості першої та другої разом = (', book_1, ' + ', book_2, ') / 2 = ', book_3, 'грн.')
book_all = book_1 + book_2 + book_3
print('Всі книги будуть коштувати: перша + друга + третя = ', book_1, '+', book_2, '+', book_3, '=', book_all, 'грн.')
print('Відповідь:', book_all, 'грн. будуть коштувати усі книги, якщо купити по одному примірнику' )