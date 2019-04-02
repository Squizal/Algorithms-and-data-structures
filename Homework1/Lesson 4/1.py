import timeit
from random import random

# Первый вариант алгоритма
N = 15
arr = [0] * N
for i in range(N):
    arr[i] = int(random() * 100)
    print(arr[i], end=' ')
print()

print("\nСтарт выполнения первого алгоритма")
start_time = timeit.default_timer()
mn = min(arr)
mx = max(arr)
imn = arr.index(mn)
imx = arr.index(mx)
print('arr[%d]=%d arr[%d]=%d' % (imn + 1, mn, imx + 1, mx))
a = (timeit.default_timer() - start_time) * 1000
print("Время выполнения:", "%.5f мс" % a)

print("\nСтарт выполнения второго алгоритма")
start_time = timeit.default_timer()
mn = 0
mx = 0
for i in range(N):
    if arr[i] < arr[mn]:
        mn = i
    elif arr[i] > arr[mx]:
        mx = i
print('arr[%d]=%d arr[%d]=%d' % (mn+1, arr[mn], mx+1, arr[mx]))
b = (timeit.default_timer() - start_time) * 1000
print("Время выполнения:", "%.5f мс" % b)
if a > b:
    print("\nВторой алгоритм быстрее")
elif a == b:
    print("\nСкорость выполнения одинаковая")
else:
    print("\nПервый алгоритм быстрее")