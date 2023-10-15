# Quick Sort
# Picks a 'pivot' element and partitions the array into two sub-arrays according to the pivot,
#  then recursively sorts the sub-arrays.
#  Runtime: O(n log n)


def quicksort(arr):
    # Base case: if the list has 1 or 0 elements, it's already sorted
    if len(arr) <= 1:
        return arr

    # Step 2: Choose a pivot (here, we choose the middle element)
    pivot = arr[len(arr) // 2]

    # Step 3: Partition the list into three parts
    left = []
    equal = []
    right = []
    for num in arr:
        if num < pivot:
            left.append(num)
        elif num == pivot:
            equal.append(num)
        else:
            right.append(num)

    # Step 4: Recursively sort the sublists of elements less than and greater than the pivot
    sorted_left = quicksort(left)
    sorted_right = quicksort(right)

    # Step 5: Combine the sorted sublists: left + equal + right
    return sorted_left + equal + sorted_right


# Example usage:
unsorted_list = [64, 34, 25, 12, 22, 11, 90]
sorted_list = quicksort(unsorted_list)

print("Sorted list:", sorted_list)
