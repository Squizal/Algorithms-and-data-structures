indst = {}
n = int(input("Введите колчество предприятий "))
s = 0
avr = 0
avr_all = 0

for i in range(n):
    sname = input(str(i + 1) + "-е предприятие: ")
    kv1 = int(input("Прибыль за 1-й квартал: "))
    kv2 = int(input("Прибыль за 2-й квартал: "))
    kv3 = int(input("Прибыль за 3-й квартал: "))
    kv4 = int(input("Прибыль за 4-й квартал: "))
    avr = kv1 + kv2 + kv3 + kv4
    indst[sname] = avr / 4
    s = s + avr / 4

avr_all = s / n

print("\nСредняя прибыль за год: %.2f. \n\nПредприятия с прибылью выше среднего:" % avr_all)
for i in indst:
    if indst[i] > avr_all:
        print(i)
print("\nПредприятия с прибылью меньше среднего:")
for i in indst:
    if indst[i] < avr_all:
        print(i)