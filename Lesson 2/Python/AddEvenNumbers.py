# Write a Python program that calculates the sum of all even numbers in a specified range [start, end],
# where start and end are integers provided by the user.

# Step 1: Prompt the user for input
start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))

# Step 2: Initialize the sum of even numbers
sum_even = 0

# Step 3: Use a for loop to iterate through the range
for num in range(start, end + 1):
    # Step 4: Check if the number is even and add it to the sum
    if num % 2 == 0:
        sum_even += num

# Step 5: Print the sum of even numbers
print("Sum of even numbers in the range:", sum_even)
