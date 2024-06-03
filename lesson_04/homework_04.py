adwentures_of_tom_sawer = """\
Tom gave up the brush with reluctance in his .... face but alacrity
in his heart. And while
the late steamer
"Big Missouri" worked ....
and sweated
in the sun,
the retired artist sat on a barrel in the .... shade close by, dangled his legs,
munched his apple, and planned the slaughter of more innocents.
There was no lack of material;
boys happened along every little while;
they came to jeer, but .... remained to whitewash. ....
By the time Ben was fagged out, Tom had traded the next chance to Billy Fisher for
a kite, in good repair;
and when he played
out, Johnny Miller bought
in for a dead rat and a string to swing it with—and so on, and so on,
hour after hour. And when the middle of the afternoon came, from being a
poor poverty, stricken boy in the .... morning, Tom was literally
rolling in wealth."""

# print(adwentures_of_tom_sawer)

print('\ntask 01 ----------------------------------------------------')
##  ПЕРЕЗАПИСУЙТЕ зміст змінної adwentures_of_tom_sawer у завданнях 1-3
# task 01 ==
""" Дані у строці adwentures_of_tom_sawer розбиті випадковим чином, через помилку.
треба замінити кінець абзацу на пробіл .replace("\n", " ")"""
adwentures_of_tom_sawer = adwentures_of_tom_sawer.replace("\n", " ")
print('adwentures_of_tom_sawer = ', adwentures_of_tom_sawer)

print('\ntask 02 ----------------------------------------------------')
# task 02 ==
""" Замініть .... на пробіл
"""
adwentures_of_tom_sawer = adwentures_of_tom_sawer.replace("....", " ")
print('adwentures_of_tom_sawer = ', adwentures_of_tom_sawer)

print('\ntask 03 ----------------------------------------------------')
# task 03 ==
""" Зробіть так, щоб у тексті було не більше одного пробілу між словами.
"""
adwentures_of_tom_sawer = adwentures_of_tom_sawer.split()
adwentures_of_tom_sawer = ' '.join(adwentures_of_tom_sawer)
print('adwentures_of_tom_sawer = ', adwentures_of_tom_sawer)

print('\ntask 04 ----------------------------------------------------')
# task 04
""" Виведіть, скількі разів у тексті зустрічається літера "h"
"""
# print(adwentures_of_tom_sawer.count('h'))
print(adwentures_of_tom_sawer.count('h'), 'разів у тексті зустрічається літера "h"')

# count = adwentures_of_tom_sawer.count('h')
# print(f'{count} разів у тексті зустрічається літера "h"')
"""
count = 0
for letter in adwentures_of_tom_sawer:
    if letter == 'h':
        count += 1
print(count)
"""
print('\ntask 05 ----------------------------------------------------')
# task 05
""" Виведіть, скільки слів у тексті починається з Великої літери?
"""
count = 0
for word in adwentures_of_tom_sawer.split():
    if word.istitle():
        count += 1
print(count, 'слів у тексті починається з великої літери')

print('\ntask 06 ----------------------------------------------------')
# task 06
""" Виведіть позицію, на якій слово Tom зустрічається вдруге
"""
index_1 = adwentures_of_tom_sawer.find('Tom')
# if index_1 !=-1:
index_2 = adwentures_of_tom_sawer.find('Tom', index_1 + 1)
print(index_2, 'позиція, на якій слово Tom зустрічається вдруге')

print('\ntask 07 ----------------------------------------------------')
# task 07
""" Розділіть змінну adwentures_of_tom_sawer по кінцю речення.
Збережіть результат у змінній adwentures_of_tom_sawer_sentences
"""
# print(adwentures_of_tom_sawer.count('.')) # 5 речень
adwentures_of_tom_sawer_sentences = None
adwentures_of_tom_sawer = adwentures_of_tom_sawer.split('. ')
print('adwentures_of_tom_sawer = ', adwentures_of_tom_sawer)

print('\ntask 08 ----------------------------------------------------')
# task 08
""" Виведіть четверте речення з adwentures_of_tom_sawer_sentences.
Перетворіть рядок у нижній регістр.
"""
print('4-е речення з adwentures_of_tom_sawer_sentences: \n', adwentures_of_tom_sawer[3])
print('4-е речення з adwentures_of_tom_sawer_sentences у нижньому регістрі: \n', adwentures_of_tom_sawer[3].lower())

print('\ntask 09 ----------------------------------------------------')
# task 09
""" Перевірте чи починається якесь речення з "By the time".
"""

for word in adwentures_of_tom_sawer:
    if word.startswith('By the time'):
        print('Є речення, яке починається з "By the time"')

print('\ntask 10 ----------------------------------------------------')
# task 10
""" Виведіть кількість слів останнього речення з adwentures_of_tom_sawer_sentences.
"""
last_sentence = adwentures_of_tom_sawer[-1]
last_sentence = last_sentence.split()
print('Кількість слів останнього речення = ', len(last_sentence))