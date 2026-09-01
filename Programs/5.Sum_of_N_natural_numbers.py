n = int(input("Enter n: "))
result = 0
for i in range(1,n+1,1):
    result += i
    if i<n:
        print(f"{i} +", end=' ')
    else:
        print(f"{i} = {result}")
        