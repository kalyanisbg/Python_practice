def bubble_sort(data):
    n = len(data)
    for i in range(n):
        swapped = False   # track if any swaps occur this 'pass'
        for j in range(n - i - 1):
            if data[j] > data[j+1]:
                print(f"list now {data}")
                print(f"swapping {data[j]} & {data[j+1]}")
                data[j], data[j+1] = data[j+1], data[j]
                swapped = True
                print("list after swap {data}")
    return data[-1]
