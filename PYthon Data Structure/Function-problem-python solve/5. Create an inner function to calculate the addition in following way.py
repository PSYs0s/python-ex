def outer_function():
    def inner_function(a,b):
        addition=a+b
        print(f"Addition:{addition}")
    inner_function(int(input("Enter first number:")),int(input("Enter second number:")))
outer_function()
