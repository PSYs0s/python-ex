total=0
count=0
while True:
    inp=int(input("Number(enter '0 to exit')>>"))
    if inp == 0:
        break
    total=total+inp
    count=count+1
print(f"Total:{total}")
print(f"Count:{count}")
print(f"Average:{total//count}")
