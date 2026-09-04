def fibonacci(n):

    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

limit = int(input("Enter the limit of series: "))

print("Fibonacci Series: ")
for number in range(1,limit):
    print(f"{fibonacci(number)}", end = ' ')