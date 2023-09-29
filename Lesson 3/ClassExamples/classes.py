# a class is a blueprint for creating objects
#  Here's the basic syntax for defining a class in Python:


class ClassName:
    # Class variables (shared by all instances of the class, if any)
    class_variable = "I am a class variable"

    # Constructor method (called when a new instance of the class is created)
    def __init__(self, parameter1, parameter2):
        self.instance_variable1 = parameter1  # Instance variable 1
        self.instance_variable2 = parameter2  # Instance variable 2

    # Instance method (can access and modify instance variables)
    def instance_method(self):
        # Do something with instance variables
        print("I am an instance method")
        print("Instance Variable 1:", self.instance_variable1)
        print("Instance Variable 2:", self.instance_variable2)


# Creating an instance of the class
object_name = ClassName("value1", "value2")

# Accessing class variables
print(ClassName.class_variable)

# Calling an instance method
object_name.instance_method()
