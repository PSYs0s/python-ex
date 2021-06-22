fName=input('Enter file name: ')
try:
    fHandle=open(fName)
except:
    print('File can not find Try again.')
    exit()
daysDic=dict()
for line in fHandle:
    line=line.rstrip()
    if line.startswith('From') and not line.startswith('From:'):
        words=line.split()
        daysDic[words[2]]=daysDic.get(words[2],0)+1
print(daysDic)