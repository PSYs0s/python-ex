def computegrade(a):
    if f_score < 0 or f_score > 1:
        print('Error')
    else:
        if f_score >= .9 :
            print('A')
        elif f_score >= .8 :
            print('B')
        elif f_score >= .7 :
            print('C')
        elif f_score >= .6 :
            print('D')
        else :
            print('F')
while True:
    score = input('Enter score:')
    try:
        f_score=float(score)
        computegrade(f_score)
    except:
        print('Bad input!')
        continue
