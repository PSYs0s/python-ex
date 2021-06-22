bignumber=None
smallnumber=None
total=0
count=0
while True:
    inp=int(input("Number(enter '-1 to exit')>>"))
    if inp == -1:
        break
    total=total+inp
    count=count+1
    if bignumber is None or inp>bignumber:
        bignumber=inp
    if smallnumber is None or inp<smallnumber:
        smallnumber=inp
print(f"Total:{total}")
print(f"Count:{count}")
print(f"Big Number:{bignumber}")
print(f"Small Number:{smallnumber}")
