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

# Popping
# print(random.pop(0))
# print(random)

# Clearing
# random.clear()
# print(random)

# duplicate = random.copy()
# print(duplicate, random)

# print(random.index(3.14))

new_list = my_number_list + fruit
# print("Adding two lists together: ", new_list)

# print(fruit[0])
# print(fruit[2])
# print(fruit[3])

# print("Fruit Count: ", len(fruit))

# fruit.append("Strawberry")
# print(fruit)

tuppaware = (
    1,
    2,
    3,
)  # tuple - Tuples are like lists except they are immutable (their values cannot be changed)

# print(tuppaware.index(1))


my_dict = {
    "name": "Alice",
    "age": 23,
    "country": "Canada",
}  # dictionary - dictonaries store key-value pairs, key values cannot be the same, but values can

# print(my_dict)
# print(my_dict["name"])
# print(my_dict.get("name"))
# print(my_dict.keys())
# my_dict.update({"city": "Toronto"})
# my_dict.update({"city": "Brampton"})
# my_dict.update({"city": "Canada"}) # you can have same values but not same key
# my_dict.clear()
# print(my_dict)

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

# TODO: Draw diagrams to visualize data structures
# Stacks are a data structure that follows LIFO - we will go over this in more detail with implementing classes and functions
# Queues are data structures that follow FIFO - we will go over this in more detail with implementing classes and functions
# Trees are hierarchical data structures consisting of nodes connected by edges (Binary Trees, Binary Search Trees, heaps)
