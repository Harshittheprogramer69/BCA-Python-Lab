number_1 = int(input("Enter the 1st number: "))
number_2 = int(input("Enter the 2nd number: "))
number_3 = int(input("Enter the 3rd number: "))

if number_1 >= number_2 and number_1 >= number_3:
    largest = number_1
elif number_2 >= number_1 and number_2 >= number_3:
    largest = number_2
else:
    largest = number_3

print(f"{largest} is the largest number.")