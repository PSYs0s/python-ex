inp=input('Enter score: ')
number=float(inp)
if number < 0.0 or number > 1.0:
    print('Error!')
if number >= 0.0 and number <= 1.0:
    if number >= 0.9 :
        print('A')
    elif number >= 0.8 :
        print('B')
    elif number >= 0.7 :
        print('C')
    elif number >= 0.6 :
        print('D')
    else :
        print('F')
