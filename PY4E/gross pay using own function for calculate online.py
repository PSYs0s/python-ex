def computepay(h,r):
    if fhrs > 40 :
        pay = (fhrs * frate) + (fhrs - 40) * (frate * .5)
    else:
        pay = fhrs*frate
    return pay

hrs = input('Enter hours:')
rate = input('Enter rate:')
fhrs = float(hrs)
frate = float(rate)
computepay(fhrs,frate)
print('Pay',computepay(fhrs,frate))
