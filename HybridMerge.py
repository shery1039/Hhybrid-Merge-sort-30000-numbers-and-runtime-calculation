# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 23:02:58 2024

@author: hp
"""

import csv
import random
import time

from BubbleSort import randomArray 

def HybridMergeSort(array, left, right, n):
    """Sort the array using hybrid merge sort with insertion sort for small arrays."""
    if right - left + 1 <= n:
        insertion_sort(array, left, right)
    else:
        mid = (left + right) // 2
        HybridMergeSort(array, left, mid, n)
        HybridMergeSort(array, mid + 1, right, n)
        MergeSort(array, left, mid, right)

def insertion_sort(array, left, right):
    """Sort a subarray using insertion sort."""
    for i in range(left + 1, right + 1):
        temp = array[i]
        j = i - 1
        while j >= left and temp < array[j]:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = temp

def MergeSort(array, left, mid, right):
    """Merge two sorted subarrays."""
    n1 = mid - left + 1
    n2 = right - mid

    left_half = array[left:mid + 1]
    right_half = array[mid + 1:right + 1]

    i = 0
    j = 0
    k = left

    # Merging the two halves
    while i < n1 and j < n2:
        if left_half[i] <= right_half[j]:
            array[k] = left_half[i]
            i += 1
        else:
            array[k] = right_half[j]
            j += 1
        k += 1

    while i < n1:
        array[k] = left_half[i]
        i += 1
        k += 1

    while j < n2:
        array[k] = right_half[j]
        j += 1
        k += 1

# Generate a random array of 30,000 integers
size = 30000
array = randomArray(size)

print("Random Array is", array[:10], "...")  # Print only a sample of the array for brevity

# Measure the runtime of the HybridMergeSort function
start_time = time.time()
left = 0
right = size - 1
n = 50  # Threshold for switching to insertion sort

HybridMergeSort(array, left, right, n)
end_time = time.time()
Run_time = end_time - start_time

# Print the sorted array and runtime
print("Sorted Array:", array[:10], "...")  # Print only a sample of the array for brevity
print("The runtime taken is", Run_time, "seconds")

# Save the sorted array to a CSV file
with open("SortedHybridSort.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Sorted Array"])
    for i in array:
        writer.writerow([i])
