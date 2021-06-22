large_number=0
small_number=0
while True :
    number=input('Enter a number(write "done" for exit) : ')
    if number=='done':
        break
    try:
        inumber=int(number)
    except:
        print('Invalid input')
        continue
    if small_number==0 :
        small_number=inumber
    elif inumber< small_number:
        small_number=inumber
    if large_number==0 :
        large_number=inumber
    elif inumber > large_number :
        large_number=inumber
print('Maximum is',large_number)
print('Minimum is',small_number)
