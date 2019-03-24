a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))
if a + b <= c or a + c <= b or b + c <= a:
    print("Существование треугольника невозможно")
elif a != b and a != c and b != c:
    print("Треугольник разносторонний")
elif a == b == c:
    print("Треугольник равносторонний")
else:
    print("Треугольник равнобедренный")