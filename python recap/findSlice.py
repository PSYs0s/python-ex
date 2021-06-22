str='X-DSPAM-Confidence:0.8475'
fColon=str.find(':')
lIndex=len(str)
tPortion=str[fColon+1:lIndex]
print(tPortion)