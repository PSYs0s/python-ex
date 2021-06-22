fName=input('Enter the file name:')
try:
    fHand=open(fName)
except:
    print('File cannot be oppened:',fName)
    exit()
count=0
for line in fHand:
    if line.startswith('Subject:'):count=count+1
print('Ther were', count,'subject lines in',fName)