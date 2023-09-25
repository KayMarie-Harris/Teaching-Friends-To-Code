# Write pseudocode to calculate and display the sum of two numbers entered by the user.

# 1. Take user input
# 2. store user input into var num 1
# 3. take user input
# 4. store user input  into var num 2
# 5. set sum to  num 1 + num 2
# 6. Display "The sum of", first_number, "and", second_number, "is", sum

num_one = input("Enter a number: ")
num_two = input("Enter a second number: ")

num_one = int(
    num_one
)  # doing this is called casting - converting a var from one type to another
num_two = int(num_two)

sum = num_one + num_two

print(num_one, " + ", num_two, " = ", sum)

# one problem with this is that is assumes that the user puts in the correct inputs, how do you think we could approach this problem?
