# Create a function that takes two numbers and calculates num1^num2


def power(num1, num2):
    # return num1**num2 #Technically this is valid but i want to practice writing out functions
    ret_val = 1

    for num in range(num2):
        ret_val = ret_val * num1
    return ret_val


print(power(5, 3))
print(5**3)
