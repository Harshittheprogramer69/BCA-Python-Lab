def filter_out_multiples(number,list_1):
    list_2 = []

    for item in list_1:
        if item % number == 0:
            list_2.append(item)

    return list_2

first_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
print(first_list)
n = int(input("Enter a number: "))
print(f"Multiples of {n} in list are: {filter_out_multiples(number=n,list_1=first_list)}")