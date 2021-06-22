inp1=input('Enter hour:')
inp2=input('Enter rate:')

try:
    hrs=float(inp1)
    rate=float(inp2)
except:
    print('Please enter numeric number!')
pay=hrs*rate
print('pay:',pay)
