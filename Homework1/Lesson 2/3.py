a = int(input("Введите число:"))
b = 0
#Нам нужно получить остаток от деления на 10, и записать его в начало новой переменной
while a>0:
    b = b*10 + a%10
    a = a//10
print(b)