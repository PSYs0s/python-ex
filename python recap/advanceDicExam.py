import string
string.punctuation

fName=input('Enter file name: ')
try:
    fHand=open(fName)
except:
    print("File cann't be open:",fName)
    exit()
counts=dict()
for line in fHand:
    line=line.rstrip()
    line=line.translate(line.maketrans('','',string.punctuation))#manually punction deleting but python do automatically
    line=line.lower()
    words=line.split()
    for word in words:
        counts[word]=counts.get(word,0)+1
print(counts)