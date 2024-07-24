# O(1) – константная сложность; сложность означает, что время выполнения алгоритма не зависит от размера входных данных

def get_element(arr, index):
    return arr[index]


# Этот алгоритм имеет константную сложность, так как время выполнения не зависит от размера массива
array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(get_element(array, 4))
print('-' * 10)


# O(n) – линейная сложность означает, что время выполнения алгоритма пропорционально количеству входных данных

def line_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


array = [10, 20, 30, 40, 50]
print(line_search(array, 30))
print(line_search(array, 60))
print('-' * 10)


# O(log n) – логарифмическая сложность алгоритма означает, что время выполнения алгоритма увеличивается логарифмически
# с увеличением размера входных данных

def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1


array = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print(binary_search(array, 70))
print(binary_search(array, 25))
