far=input('Enter Farhrenheit Temperature: ')
try:
    fFar=float(far)
    cel=(fFar-32)*5/9
    print(cel)
except:
    print('wrong key')