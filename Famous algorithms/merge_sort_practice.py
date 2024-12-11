# chop up the list into singletons

# merge by comparing the elements

[4, 5, 9, 12, 13, 10]

# first round chopping
left = [4, 5, 9]
right = [12, 13, 10]
left_left = [4] # [4, 5]
left_right = [5, 9] # [9]
right_left = [12, 13]
right_right = [10]

# second round chopping
left_left = left_left # already a singleton!

left_right_left = [5]
left_right_right = [9]
left_right = left_right_left + left_right_right

right_left_left = [12]
right_left_right = [13]
right_left = right_left_left + right_left_right

# left_left, left_right_left, left_right_right, right_left_left, right_left_right, right_right

def chop(big_list): # [4, 5, 9, 12, 13, 10]
    # base case: singleton
    if len(big_list) <= 1:
        return big_list
    # recurse
    '''
    - split in the middle into a left and right
    - recursively chop the left and right bits
    '''
    middle_index = len(big_list) // 2
    left = big_list[:middle_index]
    right = big_list[middle_index:]

    left_1 = chop(left)
    right_1 = chop(right)
    return compare_append(left_1, right_1)
    

def compare_append(list1, list2): # list1 and list2
    result = []
    while (list1 and list2):
        if list1[0] < list2[0]:
            result.append(list1[0])
            list1.pop(0)
        elif list1[0] >= list2[0]:
            result.append(list2[0])
            list2.pop(0)
    if list1:
        result += list1
    if list2:
        result += list2
    return result

ordered = chop([4, 5, 9, 12, 13, 10])
print(ordered)
