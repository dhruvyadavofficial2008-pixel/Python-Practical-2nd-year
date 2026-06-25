print("a. Finding the largest number in a list:")
numbers_a = [34, 12, 78, 56, 23]
largest = max(numbers_a)
print("List:", numbers_a)
print("Largest number:", largest)
print()

print("b. Removing duplicates from a list:")
list_with_dupes = [1, 2, 3, 2, 4, 1, 5, 3]
unique_list = list(set(list_with_dupes))  

unique_ordered = list(dict.fromkeys(list_with_dupes))
print("Original list:", list_with_dupes)
print("Unique (set, order not guaranteed):", unique_list)
print("Unique (preserving order):", unique_ordered)
print()

print("c. Counting even numbers in a list:")
numbers_c = [10, 15, 22, 33, 40, 55, 60]
even_count = sum(1 for num in numbers_c if num % 2 == 0)
print("List:", numbers_c)
print("Number of even elements:", even_count)
print()

print("d. Input 5 numbers into a list:")
input_list = []
for i in range(5):
    while True:
        try:
            num = float(input(f"Enter number {i+1}: "))
            input_list.append(num)
            break
        except ValueError:
            print("Invalid input. Please enter a number.")
print("You entered:", input_list)
print()

def average(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

print("e. Average of a list using a function:")
test_list = [10, 20, 30, 40, 50]
avg = average(test_list)
print("List:", test_list)
print("Average:", avg)
print()


print("f. Converting a string to a list of characters:")
my_string = "Hello, World!"
char_list = list(my_string)
print("String:", my_string)
print("List of characters:", char_list)
print()

print("g. Joining list elements into a single string:")
words = ["Python", "is", "awesome"]
joined_string = " ".join(words)
print("List of strings:", words)
print("Joined string:", joined_string)

numbers_list = [1, 2, 3, 4]
joined_numbers = ", ".join(str(num) for num in numbers_list)
print("List of numbers:", numbers_list)
print("Joined as string with comma:", joined_numbers)
print()

print("All list operations demonstrated.")
