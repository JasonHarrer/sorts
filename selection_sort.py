#!/usr/bin/env python

def selection_sort(array):
    for i in range(len(array)):
        min = array[i]
        pos = i
        for j in range (i, len(array), 1):
            if array[j] < min:
                min = array[j]
                pos = j
        array[i], array[pos] = array[pos], array[i]
        print(f'Current array: {array}')


test_array = [13, 3, 2, 9, 7, 8, 2, 5]

print(f'Test Array before selection_sort: {test_array}')
selection_sort(test_array)
print(f'Test Array after selection_sort:  {test_array}')

