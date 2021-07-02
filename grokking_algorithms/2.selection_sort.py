def find_smallest_index(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(len(arr)):
        if arr[i] < smallest:
            smallest_index = i
            smallest = arr[i]      
    return smallest_index

def selection_sort(arr):
    sorted_arr = []
    while arr:
        sorted_arr.append(arr.pop(find_smallest_index(arr)))
    return sorted_arr

print(selection_sort([1, 505, 2, 51, -1, 52, 50]))