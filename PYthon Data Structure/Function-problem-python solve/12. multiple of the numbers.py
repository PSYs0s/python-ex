#first we have to make lis
number_list=list()

def for_mul(a):
    mul=1
    for i in a:
        mul=mul*i
    return mul

while True:
        value=int(input("Number(enter -1 to exit)>>"))
        if value < 0:
            break
        number_list.append(value)

print(f"This is my list:{number_list}")
for_mul(number_list)
print(f"Multiple value of this list:{for_mul(number_list)}")
