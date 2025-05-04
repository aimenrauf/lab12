def selection(arr):
    n = len(arr)
    count = 0
    for i in range(n):
        min = i
        for j in range(i + 1, n):
            if arr[j] < arr[min]:
                min = j
        if min != i:
            arr[i], arr[min] = arr[min], arr[i]
            count += 1
    print(f"Total swaps: {count}")
    return arr
array = [64,23,12,72,34,67]
sorted_array = selection(array)
print("Sorted array:", sorted_array)