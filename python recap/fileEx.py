fName=input('Enter file name>>')
try:
    fHand=open(fName)
except:
    print('Enter exist file name!')
    exit()
total=0
count=0
for line in fHand:
    if line.startswith('X-DSPAM-Confidence:'):
        sPoint=line.find(':')
        length=len(line)
        value=line[sPoint+1:length-1]
        count=count+1
        total=total+float(value)
print(count)
print(total)