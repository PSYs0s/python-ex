def find_max(a,b,c):
    if num_1>num_2 and num_1>num_3:
        print(f"This number is big:{num_1}")
    elif num_2>num_1 and num_2>num_3:
        print(f"This number is big:{num_2}")
    elif num_3>num_1 and num_3>num_2:
        print(f"This number is big:{num_3}")
num_1=int(input("Enter first number:"))
num_2=int(input("Enter second number:"))
num_3=int(input("Enter third number:"))
find_max(num_1,num_2,num_3)
