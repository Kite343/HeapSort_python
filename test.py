import random

from heapSorting import heapSort


a, b = int(input("введите минимальную длину массива ")), int(input("введите максимальную длину массива "))
n = int(input("введите количество тастов "))
for _ in range(n):
    array = [random.randint(-200, 200) for _ in range(random.randint(a, b))]
    print(*array)
    heapSort(array)
    print(*array)
    print()