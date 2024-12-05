import random
# make sure the array has atleast 3 integers - if else
def three_largest(array):
    if len(array) >= 3:
        for i in range(len(array)):
            for j in range(i, len(array)):
                min_n = min(array[i], array[j])
                max_n = max(array[i], array[j])
                array[i] = min_n
                array[j] = max_n
        return array[-3:]
    else:
        print("Sorry, there should be atleast 3 elements in the array")
        return None
    

print(three_largest([9, 10, 23, 54, 21, 12, 0, -2, 4, 6, 19, 34]))

# def three_largest(array):
#     if len(array) >= 3:
#         # proceed

#     else:
#         return None
    
def sum_of_three(num):
    if num >= 3:
        a = random.randint(1, num-2)
        b = random.randint(a+1, num-1)
        return a, b - a, num - b
    else:
        return None
def slice_list(array):
    a, b, c = sum_of_three(len(array))
    list1 = array[:a]
    list2 = array[a:b]
    list3 = array[b:c]
    return list1, list2, list3

print(slice_list([4, 3, 6, 8, 2, 10, 13]))