def compute_pay(a,b):
    if a>40:
        pay=(a*b)+(a-40)*(10*.5)
    else:
        pay=a*b
    return pay
hrs=float(input("Hours>>"))
rate=float(input("Rate>>"))
pay=compute_pay(hrs,rate)
print(f"Total pay:{pay}")
