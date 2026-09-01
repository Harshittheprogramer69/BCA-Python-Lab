def generate_table(number):
    for i in range(1,11,1):
        print(f"{number} X {i} = {number*i}")

n = int(input("Enter a number: "))
generate_table(n)