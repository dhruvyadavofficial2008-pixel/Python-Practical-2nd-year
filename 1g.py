num = [12, 45, 7, 23, 89, 34, 56, 18, 90, 11]

print("Maximum:", max(num))
print("Minimum:", min(num))
print("Average:", sum(num) / len(num))

ascending = sorted(num)
print("Ascending Order:", ascending)

descending = sorted(num, reverse=True)
print("Descending Order:", descending)

num.append(100)
print("After Adding 100:", num)

num.pop(0)
print("After Removing First Item:", num)
