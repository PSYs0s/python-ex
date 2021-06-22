def calculator(a,b):
    sum=a+b
    substract=a-b
    mul=a*b
    division=a/b
    return sum,substract,mul,division
def print_lyrics():
    print('Love you so much')
    print('Why can i do for you?')
def repeat_lyrics():
    print_lyrics()
    print_lyrics()
def extra(a):
    print(a)
    print(a)
inp=input('Enter first number:')
inp2=input('Enter second number:')
fnum1=float(inp)
fnum2=float(inp2)
x=calculator(fnum1,fnum2)
print(x)
print_lyrics()
repeat_lyrics()
extra('psys0s '*4)
