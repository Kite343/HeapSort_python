import random


def heapSort(arr):
    build_heap(arr)
    for i in range(len(arr) - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, index=0, size=i)

def build_heap(arr):
    size = len(arr)
    start = (size - 2)//2
    while start >= 0:
        heapify(arr, start, size)
        start -= 1

def heapify(arr, index, size):
    left = 2*index + 1
    right = 2*index + 2
    if (left < size and arr[left] > arr[index]):
        largest = left
    else:
        largest = index
    if (right < size and arr[right] > arr[largest]):
        largest = right
    if (largest != index):
        arr[largest], arr[index] = arr[index], arr[largest]
        heapify(arr, largest, size)

# array = [1, 7, -3, 9, 0, -67, 34, 12, 45, 100, 6,  8, -2, 99]
# print(array)
# heapSort(array)
# print(array)

# test
a, b = int(input("введите минимальную длину массива ")), int(input("введите максимальную длину массива "))
n = int(input("введите количество тастов "))
for _ in range(n):
    array = [random.randint(-200, 200) for _ in range(random.randint(a, b))]
    print(*array)
    heapSort(array)
    print(*array)
    print()
