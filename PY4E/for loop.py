inp='aabbdsjaabhsha'
count=0
op=0
for number in inp:
    count=count+1
    print(count,number)
for number in inp:
    if number == 'a':
        op=op+1
print(op)
