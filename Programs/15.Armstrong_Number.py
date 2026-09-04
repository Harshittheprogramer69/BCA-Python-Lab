def is_armstrong(number):
    original_number = number
    digit_count = 0
    armstrong_sum = 0
    temporary_number = number
    while temporary_number > 0:
        digit_count += 1
        temporary_number //= 10
    temporary_number = number
    while temporary_number > 0:
        digit = temporary_number % 10
        armstrong_sum += digit ** digit_count
        temporary_number //= 10
    return original_number == armstrong_sum


user_number = int(input("Enter a number: "))

if is_armstrong(user_number):
    print("Armstrong number")
else:
    print("Not an Armstrong number")