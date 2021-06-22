print("Enter '0' in both option  to exit, ASAP\n")
while True:
    inp1=input("Enter hour:")
    inp2=input("Enter rate:")
    try:
        hrs=float(inp1)
        rate=float(inp2)
        if hrs <=0 and rate<=0:
            break
        print("\nValue is valid!")
    except:
        print("\nEnter valid value!\n")
        continue
    if hrs > 40:
        pay=(hrs*rate)+(hrs-40)*(rate*.5)
    else:
        pay=hrs*rate
    print(f"Pay:{pay}\n")
