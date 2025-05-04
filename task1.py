def bubble(array):
    n = len(array)
    for i in range(n):
        swapped = False  
        for j in range(0, n - i - 1):
            if array[j] > array[j + 1]:               
                array[j], array[j + 1] = array[j + 1], array[j]
                swapped = True       
        if not swapped:
            break
    return array

array1 = [5, 1, 4, 2, 8]
print(bubble(array1))  