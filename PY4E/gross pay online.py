hrs=input('Enter hours:')
rate=input('Enter rate:')
flost_hrs=float(hrs)
flost_rate=float(rate)
if flost_hrs > 40 :
    pay = (flost_hrs*flost_rate)+(flost_hrs-40)*(flost_rate*.5)
else :
    pay = flost_hrs*flost_rate
print(pay)
