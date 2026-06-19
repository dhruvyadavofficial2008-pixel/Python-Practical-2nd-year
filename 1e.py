def swap_elements(self, i, j):
    self[i], self[j] = self[j], self[i]
    return self

numbers = list(map(int, input("Enter list elements separated by spaces: ").split()))

i = int(input("Enter index num 1: "))
j = int(input("Enter index num 2: "))

swap_elements(numbers, i, j)
print("Updated List:", numbers)
