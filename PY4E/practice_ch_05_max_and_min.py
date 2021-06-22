big_number=None
small_number=None
for i in [1,2,3,4,7,6]:
    if big_number is None or i> big_number:
        big_number=i
    if small_number is None or i< small_number:
        small_number=i
print(big_number)
print(small_number)
