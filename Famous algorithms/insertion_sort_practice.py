def insertion_sort(arr):
    # start of sorted region: initially 0
    # compare the first element of unsorted region with every element of 
    # get the start index of unsorted region
    for sorted_index in range(0, 1):
        for unsorted_index in range(1, len(arr)):
            if arr[sorted_index] > arr[unsorted_index]:
                arr[sorted_index], arr[unsorted_index] = arr[unsorted_index], arr[sorted_index]
    return arr
    # loop through each element of unsorted region
    # for each element for unsorted region, compare to each element of sorted region
    # if current unsorted element < current sorted element, replace current sorted element index with current unsorted element


def insertion_sort(arr):
    for i in range(1, len(arr)):
        focus = arr[i]
        '''
        focus: current element in the unsorted region we want to insert into the 
        correct position in the sorted region
        '''
        j = i - 1
        for j in range(i - 1, -1, -1):
            if arr[j] > focus:
                # whichever index focus is at is made a copy of j
            j -= 1
            arr[j] = focus

    return arr
