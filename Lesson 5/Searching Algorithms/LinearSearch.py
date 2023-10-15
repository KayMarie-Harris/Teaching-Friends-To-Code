# Linear/Selective search
#  Move sequentially until items found
# Time Complexity: O(n) TODO: Draw graph so students can see the difference in time complexity


def linear_search(arr, target):
    for element in arr:
        if element == target:
            return True  # Element found
    return False  # Element not found in the list


# Example usage:
arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
target = 9
if linear_search(arr, target):
    print(f"Element {target} found in the list.")
else:
    print(f"Element {target} not found in the list.")
