import random
import time
import copy

def quick_last(arr, low, high, counter):
    if low < high:
        pi, counter = partition_last(arr, low, high, counter)
        counter = quick_last(arr, low, pi - 1, counter)
        counter = quick_last(arr, pi + 1, high, counter)
    return counter

def partition_last(arr, low, high, counter):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        counter += 1
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1, counter

def quick_first(arr, low, high, counter):
    if low < high:
        pi, counter = partition_first(arr, low, high, counter)
        counter = quick_first(arr, low, pi - 1, counter)
        counter = quick_first(arr, pi + 1, high, counter)
    return counter

def partition_first(arr, low, high, counter):
    pivot = arr[low]
    i = low + 1
    for j in range(low + 1, high + 1):
        counter += 1
        if arr[j] < pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[low], arr[i - 1] = arr[i - 1], arr[low]
    return i - 1, counter

def timing(sort_func, arr):
    data_copy = copy.deepcopy(arr)
    start = time.time()
    counter = sort_func(data_copy, 0, len(data_copy) - 1, 0)
    end = time.time()
    duration = (end - start) * 1000  # ms
    return duration, counter

array = [random.randint(1, 1000) for _ in range(500)]
print("Quick Sort Comparison on 500 random numbers:\n")

time_last, steps_last = timing(quick_last, array)
print("Quick Sort (Last Element as Pivot):")
print(f"  Time Taken     = {time_last:.2f} ms")
print(f"  Comparisons    = {steps_last}\n")

time_first, steps_first = timing(quick_first, array)
print("Quick Sort (First Element as Pivot):")
print(f"  Time Taken     = {time_first:.2f} ms")
print(f"  Comparisons    = {steps_first}")
