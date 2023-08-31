import random

array_size = 10
random_array = [random.randint(1, 100) for _ in range(array_size)]

# Сортировка Bubble Sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

bubble_sorted = random_array.copy()
bubble_sort(bubble_sorted)
print("Отсортерованный массив Bubble Sorted:", bubble_sorted)

# Сортировка Selection Sort
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

selection_sorted = random_array.copy()
selection_sort(selection_sorted)
print("Отсортированный массив Selection Sort:", selection_sorted)

# Сортировка Insertion Sort
def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

insertion_sorted = random_array.copy()
insertion_sort(insertion_sorted)
print("Отсортерованный массив Insertion Sorted:", insertion_sorted)

# Сортировка Merge Sort
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

merge_sorted = random_array.copy()
merge_sort(merge_sorted)
print("Отсортированный массив Merge Sorted:", merge_sorted)