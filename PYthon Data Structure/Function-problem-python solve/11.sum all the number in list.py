#first we have to make lis
number_list=list()

def for_add(a):
    add=0
    for i in a:
        add=add+i
    return add

while True:
        value=int(input("Number(enter -1 to exit)>>"))
        if value < 0:
            break
        number_list.append(value)

print(f"This is my list:{number_list}")
for_add(number_list)
print(f"Sum value of this list:{for_add(number_list)}")
