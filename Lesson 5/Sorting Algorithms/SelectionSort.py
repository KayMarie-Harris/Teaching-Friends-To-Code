# Selection sort
# Finds smallest element and moves it to the front until sorted
# Runtime: O(n^2)


def selection_sort(arr):
    n = len(arr)

    # Traverse through all elements in the list
    for i in range(n):
        # Find the minimum element in the unsorted part of the list
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        # Swap the found minimum element with the first element
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr


# Example usage:
unsorted_list = [64, 34, 25, 12, 22, 11, 90]
sorted_list = selection_sort(unsorted_list)

print("Sorted list:", sorted_list)
