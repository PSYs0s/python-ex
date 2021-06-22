score = input('Enter score:')
f_score=float(score)
if f_score < 0 :
    print('Error')
    quit()
if f_score > 1 :
    print('Error')
    quit()
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
