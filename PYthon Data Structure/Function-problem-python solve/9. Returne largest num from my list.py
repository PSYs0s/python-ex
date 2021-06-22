def find_big():
    bignumber=None
    my_list=[4, 10, 8, 24, 12, 2]
    for i in my_list:
        if bignumber is None or bignumber<i:
            bignumber=i
    return bignumber
value=find_big()
print(f"Bignumber is:{value}")
# easiest way print(max(my_list))
