# Bubble Sort
def bubble_sort(arr):
    """
    Sorts an array using Bubble Sort.
    Time Complexity: O(n^2) in worst and average case, O(n) in best case (already sorted).
    Space Complexity: O(1) (in-place sorting).
    """
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


# Merge Sort
def merge_sort(arr):
    """
    Sorts an array using Merge Sort.
    Time Complexity: O(n log n) in all cases.
    Space Complexity: O(n) (additional space for merging).
    """
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = merge_sort(arr[:mid])
        right_half = merge_sort(arr[mid:])
        return merge(left_half, right_half)
    return arr


def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


# Quick Sort
def quick_sort(arr):
    """
    Sorts an array using Quick Sort.
    Time Complexity: O(n log n) on average, O(n^2) in worst case (rare).
    Space Complexity: O(log n) due to recursion stack.
    """
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)


# Insertion Sort
def insertion_sort(arr):
    """
    Sorts an array using Insertion Sort.
    Time Complexity: O(n^2) in worst and average case, O(n) in best case (already sorted).
    Space Complexity: O(1) (in-place sorting).
    """
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


# Selection Sort
def selection_sort(arr):
    """
    Sorts an array using Selection Sort.
    Time Complexity: O(n^2) in all cases.
    Space Complexity: O(1) (in-place sorting).
    """
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr
