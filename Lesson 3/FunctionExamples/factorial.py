# Create a function that calculates the factorial of a number
# Ex: factorial(5) -> Output: 120 (since 5! = 5 × 4 × 3 × 2 × 1 = 120)
# Ex: factorial(0) -> Output: 1 (since 0! = 1)


def factorial(num):
    ret_val = 1
    curr_num = num

    while curr_num > 0:
        ret_val = ret_val * curr_num
        curr_num -= 1

    return ret_val


print(factorial(5))
print(factorial(0))
