number=input('Enter a number:')

try:
    is_number = int(number)
except:
    is_number = -1

if is_number > 0:
    print('Nice work.This is a number')
else:
    print('This is not a number')
