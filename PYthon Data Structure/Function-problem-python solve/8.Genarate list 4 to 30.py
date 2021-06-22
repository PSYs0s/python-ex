even_list=list()
n=30
def make_even_list(n):
    while n<=30:
        if n<=3:
            break
        if n%2==0:
            even_list.append(n)
        n=n-1
make_even_list(n)
print(sorted(even_list))
