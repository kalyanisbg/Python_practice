def selection_sort(arr):
    # find the start index of the unsorted list
    for i in range(len(arr)):
        min_index = i
        # find the
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr
    # the smallest is swapped for the start index of the unsorted list
    # the new start indesx becomes old index + 1 and repeat

print(selection_sort([4, 8, 2, 10, 5, 2, 0, -1, 3, 6, 2, -4]))

print(selection_sort([5, 3, 4, 1, 0, 24, 12, -4]))