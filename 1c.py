import math

while True:
    try:
        num = input("Enter a number (or type 'e' to quit): ")

        if num.lower() == "e":
            break

        num = float(num)

        if num < 0:
            print("Square root of a negative number is not a real number.")
        else:
            print("Square root =", math.sqrt(num))

    except ValueError:
        print("Invalid number! Please enter a valid number.")
