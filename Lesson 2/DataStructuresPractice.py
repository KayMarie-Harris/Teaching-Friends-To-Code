# TODO: Finish Data Structure Examples


# list - a list is an ordered collection of elements
my_number_list = [
    1,
    2,
    3,
]  # this is a list of ints, each item in a list has a position starting at 0

fruit = ["apple", "mango", "pineapple"]  # this is a list of strings
random = [
    "a",
    "pizza",
    3.14,
    9,
]  # this is a list of multiple data types... note this is not possible in all languages but we'll go into more detail further down the line

new_list = my_number_list + fruit
# print("Adding two lists together: ", new_list)

# print(fruit[0])
# print(fruit[2])
# print(fruit[3])

tuppaware = (
    1,
    2,
    3,
)  # tuple - Tuples are like lists except they are immutable (there values cannot be changed)

my_dict = {
    "name": "Alice",
    "age": 23,
    "city": "Toronto",
}  # dictionary - dictonaries store key-value pairs, key values cannot be the same, but values can

print(my_dict)
print(my_dict["name"])

my_set = set([1, 2, 3])  # set - a set is a list of unique values

# print("my_number_list: ", my_number_list)
# my_number_list.append(4)
# print("my_number_list w 4 appended: ", my_number_list)
# my_number_list.append(4)
# print("my_number_list w 4 appended (again): ", my_number_list)

# print("my_set: ", my_set)
# my_set.add(4)
# print("my_set adding 4: ", my_set)
# my_set.add(4)
# print("my_set trying to add 4 again", my_set)
