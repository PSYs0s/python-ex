def calculation(number_1,number_2):
    add=number_1+number_2
    sub=number_1-number_2
    return add,sub
inp1=int(input("Enter first number:"))
inp2=int(input("Enter seond number:"))
calculation(inp1,inp2)
print(f"(Addition , Subtracction)={calculation(inp1,inp2)}")
