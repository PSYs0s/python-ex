fhand=open('mbox-short.txt', 'r')
count=0
for line in fhand:
    line=line.rstrip()
    if line.startswith('From '):
        words=line.split()
        addres=words[1]
        print(addres)
        count=count+1
print('There were',count,'lines in the file with From as the first word')
