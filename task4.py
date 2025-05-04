import random
import time
import copy
original_data = [random.randint(1, 1000) for _ in range(500)]
def bubble(arr):
    n = len(arr)
    count = 0
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            count += 1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr, count

def selection(arr):
    n = len(arr)
    count = 0
    for i in range(n):
        min = i
        for j in range(i + 1, n):
            count += 1
            if arr[j] < arr[min]:
                min = j
        if min != i:
            arr[i], arr[min] = arr[min], arr[i]
    return arr, count

def insertion(arr):
    n = len(arr)
    count = 0
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            count += 1
            arr[j + 1] = arr[j]
            j -= 1
        count += 1  
        arr[j + 1] = key
    return arr, count

def timing(sort_func, data):
    data_copy = copy.deepcopy(data)
    start = time.time()
    _, iterations = sort_func(data_copy)
    end = time.time()
    duration = (end - start) * 1000  
    return duration, iterations

print("Sorting 500 random numbers...\n")
for name, func in [("Bubble Sort", bubble),
                   ("Selection Sort", selection),
                   ("Insertion Sort", insertion)]:
    time_taken, steps = timing(func, original_data)
    print(f"{name}:")
    print(f"  Time Taken     = {time_taken:.2f} ms")
    print(f"  Iterations     = {steps}\n")