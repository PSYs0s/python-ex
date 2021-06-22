while True:
    hrs=float(input("Enter hour(press '0' to exit):"))
    if hrs==0:
        quit()
    rate=float(input("Enter rate:"))
    if hrs<=40:
        pay=hrs*rate
    else:
        pay=(hrs*rate)+(hrs-40)*(rate*.5)
    print(f"Pay:{pay}")
