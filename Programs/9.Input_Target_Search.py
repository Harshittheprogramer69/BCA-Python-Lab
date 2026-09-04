def Linear_Search(n,list_1):
    if n in list_1:
        print(f"The {n} exists in {list_1}.")
        print(f"Index:- {list_1.index(n)+1}")
    else:
        print(f"The {n} does not exists in {list_1}.")

first_list = [1,2,3,4,5,6,7,8,9]
number = int(input("Enter a nummber: "))

Linear_Search(n=number, list_1=first_list)