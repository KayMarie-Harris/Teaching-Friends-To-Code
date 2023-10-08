import array as arr

# how you would create an array
# arr.array()

# general syntax
# variable_name = array(typecode,[elements])

numbers = arr.array("i", [10, 20, 30])

print(numbers[0])  # gets the 1st element
print(numbers[1])  # gets the 2nd element
print(numbers[2])  # gets the 3rd element

print(numbers.index(10))  # Find index of 10
