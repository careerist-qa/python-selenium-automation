def selection_sort_descending(arr):
    n = len(arr)

    for i in range(n - 1):
        max_index = i

        for j in range(i + 1, n):
            if arr[j] > arr[max_index]:
                max_index = j

        arr[i], arr[max_index] = arr[max_index], arr[i]


my_array = [64, 34, 25, 12, 22, 11, 90]
selection_sort_descending(my_array)
print("Sorted array in descending order:", my_array)

def bubble_sort_descending(arr):
    n = len(arr)

    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arr[j] < arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


my_array = [23, 47, 58, 19, 13, 27, 65]
bubble_sort_descending(my_array)
print("Sorted array in descending order:", my_array)

def insertion_sort_descending(arr):
    n = len(arr)

    for i in range(1, n):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] < key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key


my_array = [65, 47, 29, 15, 38, 20, 94]
insertion_sort_descending(my_array)
print("Sorted array in descending order:", my_array)


