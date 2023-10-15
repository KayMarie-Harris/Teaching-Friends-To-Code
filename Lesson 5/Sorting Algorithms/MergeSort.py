# Merge Sort
# cuts list into sub lists and compares
# Runtime: O(n log n)


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    # Split the input list into two halves
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Recursive call to sort the left and right halves
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    # Merge the sorted halves
    return merge(left_half, right_half)


def merge(left, right):
    merged = []
    left_index, right_index = 0, 0

    # Compare elements in both lists and merge them in sorted order
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    # Add remaining elements, if any, from both lists
    merged.extend(left[left_index:])
    merged.extend(right[right_index:])

    return merged


# Example usage:
unsorted_list = [64, 34, 25, 12, 22, 11, 90]
sorted_list = merge_sort(unsorted_list)

print("Sorted list:", sorted_list)
