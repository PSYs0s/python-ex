# l=[2,3,4,5,6]
# print(max(l))
# print(min(l))
largest=None
print('Before:',largest)
for i in [4,6,2,7,9]:
    if largest is None or i>largest:
        largest=i
    print('Loop:',i,largest)
print('Largest:',largest)

smallest=None
print('Before:',largest)
for i in [4,6,2,7,9]:
    if smallest is None or i<smallest:
        smallest=i
    print('Loop:',i,smallest)
print('Smallest:',smallest)