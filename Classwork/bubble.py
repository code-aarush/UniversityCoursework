import random

def bubble(arr):
    for i in range (len(arr) - 1):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

my_arr = [random.randint(0, 100) for i in range(10)]

bubble(my_arr)

print(my_arr)