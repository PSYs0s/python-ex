def computeGrade(n):
    if(n>=0.9):
        print('A')
    elif(n>=0.8):
        print('B')
    elif(n>=0.7):
        print('C')
    elif(n>=0.6):
        print('D')
    else:
        print('F')
point=input('Enter your grade point>>')
try:
    fPoint=float(point)
    computeGrade(fPoint)
except:
    print('Wrong input!')
