import random
print("Введите границы целых чисел (a и b) для генерация случайного числа:")
a = int(input("\tЛевая граница = "))
b = int(input("\tПрава граница = "))
print("Случайное целое число в заданном диапазоне:", random.randint(a, b))

print("\n")

print("Введите границы чисел (a и b) для генерация случайного числа:")
a = float(input("\tЛевая граница = "))
b = float(input("\tПрава граница = "))
print("Случайное вещественное число в заданном диапазоне:", random.uniform(a, b))

print("\n")

print("Введите границы символов (a и b) для генерация случайного символа:")
a = ord(input("\tЛевая граница = "))
b = ord(input("\tПрава граница = "))
print("Случайный символ в заданном диапазоне:", chr(random.randint(a, b)))