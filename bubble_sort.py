#!/usr/bin/env python

def bubble_sort(array):
    for i in range(len(array), 1, -1):
        for j in range(i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
        print(f'Current array: {array}')


test_array = [13, 3, 2, 9, 7, 8, 2, 5]

print(f'Test Array before bubble_sort: {test_array}')
bubble_sort(test_array)
print(f'Test Array after bubble_sort:  {test_array}')
