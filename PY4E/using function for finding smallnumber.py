def number(a):
    small=None
    for value in a:
        if small is None or value < small:
            small=value
    return small
    print(a)
a=[1,2,3,4,5]
number(a)
print(number(a))
