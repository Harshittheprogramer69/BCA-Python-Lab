# Write a code to find if number is even or odd

number = input("Enter your number: ")
number = int(number) 

if number % 2 == 0:
    print(f"{number} is even")
else:
    print(f"{number} is odd")