class Animal:
    # Class variable
    animal_type = "Unknown"

    # Constructor method
    def __init__(self, name, sound):
        # Instance variables
        self.name = name
        self.sound = sound

    # Instance method to make the animal sound
    def make_sound(self):
        print(f"The {self.animal_type} named {self.name} says {self.sound}")


# Creating instances of the Animal class
lion = Animal("Lion", "Roar")
dog = Animal("Dog", "Bark")

# Accessing class variable
print("Animal Type:", Animal.animal_type)

# Calling instance methods
lion.make_sound()  # Output: The Unknown named Lion says Roar
dog.make_sound()  # Output: The Unknown named Dog says Bark
