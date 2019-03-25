#Задаём диапозон значений с 32 по 128 символ
for i in range(32, 128):
    print("%4i - %s" % (i, chr(i)), end=" |")
    if i % 10 == 0:
        print("")
print("\n\n\tThe end!")