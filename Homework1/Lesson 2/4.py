n = int(input("Введите количество элементов:"))
#Начальный элемент по условия задачи 1
a = 1
b = 0
for i in range(n):
    b += a
#Каждое последующий элемент меньше предыдущего в -2 раза
    a /= -2
print(b)