x = int(input("Введите трёхзначное число:"))

a = x // 100
b = (x // 10) % 10
c = x % 10

print(a + b + c)
print(a*b*c)
