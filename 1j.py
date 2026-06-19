print("Squares of numbers from 1 to 10:")
for i in range(1, 11):
    print(i, "->", i ** 2)

even_count = 0

for i in range(5):
    num = int(input(f"Enter number {i+1}: "))
    if num % 2 == 0:
        even_count += 1

print("Number of even numbers:", even_count)
