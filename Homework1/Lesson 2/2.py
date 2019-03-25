x = int(input("Введите число:"))
chet = 0
nechet = 0
while x>0:
    if x%2 == 0:
        chet += 1
    else:
        nechet += 1
    x = x//10
print("Четных цифр - %d, нечетных цифр - %d" % (chet, nechet))