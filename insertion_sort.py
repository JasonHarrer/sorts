#!/usr/bin/env python

def insertion_sort(array):
    # Start from left and work our way right
    for i in range(1, len(array)):
        # check to see if the one to the left is greater than current
        # if so, we'll begin the sort process
        if array[i] < array[i-1]:
            #store current value
            temp = array[i]
            # shift to the right until the numbers are no longer greater
            # then insert temp
            j = i-1
            while j >= 0:
                if array[j] >= temp:
                    array[j+1] = array[j]
                    # If we are all the way to the left, then change
                    #   the first item to temp
                    if j == 0:
                        array[j] = temp
                    j = j - 1
                else:
                    # Otherwise insert when no longer greater than temp
                    array[j+1] = temp
                    j = -1


test_array = [13, 3, 2, 9, 7, 8, 2, 5]

print(f'Test Array before insertion_sort: {test_array}')
insertion_sort(test_array)
print(f'Test Array after insertion_sort:  {test_array}')
