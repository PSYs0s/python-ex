fName=input('Enter the file name: ')
try:
    fHand=open(fName)
except:
    print("File can't found! Try again")
    exit()

wordDic=dict()

for sen in fHand:
    spliting=sen.split()
    for w in spliting:
        wordDic[w]=wordDic.get(w,0)+1
        # if w not in wordDic:
        #     wordDic[w]=1
        # else:
        #     wordDic[w]=wordDic[w]+1
print(wordDic)