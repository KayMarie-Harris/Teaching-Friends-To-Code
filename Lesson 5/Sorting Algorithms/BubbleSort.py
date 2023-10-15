# Bubble Sort
# Swaps each pair until items are sorted
# Runtime: O(n^2)


def bubble_sort(arr):
    n = len(arr)

    # Traverse through all elements in the list
    for i in range(n):
        # Last i elements are already sorted, so we don't need to check them
        for j in range(0, n - i - 1):
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # Swap elements

    return arr


# Example usage:
unsorted_list = [64, 34, 25, 12, 22, 11, 90]
sorted_list = bubble_sort(unsorted_list)

print("Sorted list:", sorted_list)
