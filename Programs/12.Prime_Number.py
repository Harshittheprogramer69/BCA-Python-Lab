# Check whether a number is prime

def is_prime(n):
    is_prime = True
    if n<=1:
        is_prime = False
    else:
        for i in range(2,n):
            if n % i == 0:
                is_prime = False
                break

    return is_prime

number = int(input("Enter a number: "))

if is_prime(number):
    print(f"The {number} is a prime number.")
else:
    print(f"The {number} is a composite number.")
