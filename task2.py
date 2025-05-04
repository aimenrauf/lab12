def insertion(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
        print(f"Iteration {i}: {arr}")
    return arr

array = [5,2,6,8,3,9,12,1]
insertion(array)