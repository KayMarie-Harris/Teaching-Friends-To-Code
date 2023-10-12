# # A function is like a miniprogram within a program
# # print(), len(), and input() are all function calls, but we can also create our own

# def hello():
#     greeting = "howdy"
#     return greeting

# my_greeting = hello()

x = 0

def add(num1):
    z = x + num1
    print(z)

add(1)
print(x)

# my_sum = add(3,4)
# print(my_sum)

# my_new_num = add(my_num, 3)
# print(my_new_num)



# # Lets create a function called hello, that prints out a greeting
# def hello():
#     print("Howdy!")


# # now lets call our function
# hello()


# # When using print() or len() you have to pass them values, these are called arguments
# # Lets create a function that has a parameter


# # ------>(name)<------ this is a parameter
# def hello(name):
#     print("Hi, " + name)


# # --->("Syco")<--- this is an argument
# hello("Syco")
# my_name = "Kay"  # This is an argument

# hello(my_name)  # notice the my_name and name variables are different
# # 'name' within the functional call is a PARAMETER- a variable name that represents an argument that needs to be passed
# # 'my_name' variable is an ARGUMENT which represents the DATA PASSED to the function
# # therefore they do not have to share the same name

# # A parameter is the variable listed inside the parentheses in the function definition.
# # An argument is the value that are sent to the function when it is called.

# # my_name should NOT be used inside the function because it represents something different
# # Ex:


# def hello(name):
#     print(name)
#     print("Hello, " + my_name)


# hello("Gurjot")

# # Now we can see how functions work using print statments, but from a coding perspective, print is useful in debugging,
# # but it dosen't help pass down a value


# def my_function(x):  # x is a parameter
#     print(x)


# y = my_function(9)
# print("y =", y)

# z = print("z =", 9)
# print(z)

# # instead we will use returns
# import random  # the import statement is used to include external modules or libraries in your code.

# #               This can include functions, classes, and variables.


# def get_fortune(randNumber):
#     if randNumber == 1:
#         return "It is likely"
#     elif randNumber == 2:
#         return "Answer unknown, ask again later"
#     elif randNumber == 3:
#         return "definitly not"


# num = random.randint(1, 3)

# print(get_fortune(num))

# # or

# my_fortune = get_fortune(num)  # essentially return lets the completion of a function to assign a value

# print(my_fortune)


# def add(num1, num2):  # A function can take multiple parameters
#     return num1 + num2


# print(add(6, 9))

# # note that the standalone function() is a function, not to be confused with a method...
# # a method is a call made alongside an object (we'll go more into objects later) some methods we have seen before:
# # .add(), .append(), .index(), etc. notice the ".", because methods will always be attached to a variable/obj
