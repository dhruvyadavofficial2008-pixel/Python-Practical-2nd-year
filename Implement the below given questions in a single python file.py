
print("a. Creating a tuple with 5 different elements:")
my_tuple = (10, "hello", 3.14, True, 'world')
print("Tuple:", my_tuple)
print()

print("b. Accessing first and last elements:")
first = my_tuple[0]
last = my_tuple[-1]
print("First element:", first)
print("Last element:", last)
print()


print("c. Slicing to get the middle 3 elements:")
middle_tuple = my_tuple[1:4] 
print("Middle 3 elements:", middle_tuple)
print()

print("d. Concatenating two tuples:")
tuple1 = (1, 2, 3)
tuple2 = ('a', 'b', 'c')
concatenated = tuple1 + tuple2
print("Concatenated tuple:", concatenated)
print()

print("e. Reversing a tuple using slicing:")
reversed_tuple = my_tuple[::-1]
print("Original tuple:", my_tuple)
print("Reversed tuple:", reversed_tuple)
print()

print("f. Counting occurrences of an element in a tuple:")
sample_tuple = (1, 2, 3, 2, 4, 2, 5)
count_2 = sample_tuple.count(2)
print("Tuple:", sample_tuple)
print("Occurrences of 2:", count_2)
print()

print("g. Finding the index of a specific element:")
try:
    index = sample_tuple.index(4)
    print("Index of element 4 in tuple:", index)
except ValueError:
    print("Element not found")
print()

print("h. Checking if an element exists in a tuple:")
element = 3
exists = element in sample_tuple
print(f"Does {element} exist in {sample_tuple}? {exists}")
element = 10
exists = element in sample_tuple
print(f"Does {element} exist in {sample_tuple}? {exists}")
print()

print("i. Converting a list to a tuple:")
my_list = [5, 6, 7, 8]
converted_tuple = tuple(my_list)
print("Original list:", my_list)
print("Converted tuple:", converted_tuple)
print()

print("j. Sorting a tuple of numbers in ascending order:")
num_tuple = (9, 1, 5, 3, 7, 2)
sorted_tuple = tuple(sorted(num_tuple))  
print("Original tuple:", num_tuple)
print("Sorted tuple:", sorted_tuple)
print()

print("k. Repeating a tuple 3 times:")
repeat_tuple = (1, 2) * 3
print("Tuple repeated 3 times:", repeat_tuple)
print()

print("l. Checking immutability (trying to modify an element):")
try:
    my_tuple[0] = 99
except TypeError as e:
    print("Error caught as expected:", e)
else:
    print("Unexpected modification succeeded (should not happen).")
print()

print("All tuple operations demonstrated.")
