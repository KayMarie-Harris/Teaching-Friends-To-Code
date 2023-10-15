# Binary Search
# Splits data in half until item is found\
# Required data is sorted
# Time complexity: O(log n)


def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2  # Find the middle element
        if arr[mid] == target:
            return True  # Element found
        elif arr[mid] < target:
            left = mid + 1  # Discard left half
        else:
            right = mid - 1  # Discard right half

    return False  # Element not found in the list


# Example usage:
arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
target = 11
if binary_search(arr, target):
    print(f"Element {target} found in the list.")
else:
    print(f"Element {target} not found in the list.")
