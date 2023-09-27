# When coding you can define variables of many different data types

x = "Hello World!"  # x is a variable of type string
# A string is used to represent a text or a sequence of characters
# "123", "Python", & "I want to die" are all strings


y = "Hello"
z = " World"

# print(y + z)  # you can add strings together

# you can also redefine a variable

x = "Redefined X"

# print("x = ", x)

# all of the variables above are examples of a string, lets explore some other data types

x = 9  # int - integer data types include numbers positive & negative
# '5', '-10', and '0' are all integers (note in some languges an int and an Integer are two differnt data types)

# num = x + 7
# print("my num: ", num)
# num = x - 7
# print("my num: ", num)
# num = x / 7
# print("my num: ", num)
# num = x % 7  # modular - outputs the remainder of nums divided
# print("my num: ", num)
# num = x * 7
# print("my num: ", num)

# Variables can also be named almost anything, they don't just have to be letters, but there are certain naming conventions
# variables should use lowercase letters and underscores
# names should be meaningful

var = 3.14  # float - floating-point data types represent numbers w decimal points.
# '0.5', '4.20', and '-6.9' are all floating-points

int_plus_float = x + var
# print("adding an int and a float creates a %s data type" % type(int_plus_float))

is_true = True  # bool - booleans are variables of 'True' or 'False'

x = None  # None - none is a data type that represents the absence of a value, aka a 'null' value

txt_input = input("this allows a user to input a value. Enter any text: ")

print("The user inputed ", txt_input)
