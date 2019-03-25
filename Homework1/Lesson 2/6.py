from random import random
quest = round(random() * 100)
i = 1
print("Угадайте число используя 10 попыток")
while i <= 10:
    a = int(input(str(i) + '-я попытка: '))
    if a > quest:
        print("Меньше")
    elif a < quest:
        print("Больше")
    else
        print('Вы угадали с %i-й попытки' % i)
        break
    i += 1
else:
    print("Вы проиграли! Это было число:", quest)