fHand=open('mbox-short.txt')
for line in fHand:
    line=line.rstrip()
    if line.find('@uct.ac.za')==-1:continue
    print(line)