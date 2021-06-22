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
        daysDic[words[1]]=daysDic.get(words[1],0)+1
maxVal=None
maxKey=None
for key in daysDic:
    if maxVal is None or maxVal < daysDic[key]:
        maxVal=daysDic[key]
        maxKey=key
print(maxKey,maxVal)