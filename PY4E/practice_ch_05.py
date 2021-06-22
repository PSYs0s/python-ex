n=0
while n<=5:
    print(n,end=" ")
    n=n+1
print('Done')

while True:
    inp=input("Name>>")
    if inp == "done":
        break
    print(inp)
print("Done")

total=0
for i in [1,2,3,4,5]:
    total=total+i
print(total)
