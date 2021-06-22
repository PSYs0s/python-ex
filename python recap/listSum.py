numList=list()
while True:
    inp=input('Enter number: ')
    if inp == 'done':break
    value=float(inp)
    numList.append(value)
print('Total sum: ',sum(numList),' and total length: ',len(numList))