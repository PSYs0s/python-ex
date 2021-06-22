print('Please enter right exact file name!')
fname=input('>')
fhandle=open(fname, 'r')
count=dict()
for line in fhandle:
    if line.startswith('From '):
        words=line.split()
        name=words[1]
        if not name in count:
            count[name]=count.get(name,0)+1
        else:
            count[name]=count[name]+1


newlist=list()                  '''we can use sorted([(v,k) for (k,v) in count.items()])'''
for (k,v) in count.items():
    newtop=(v,k)
    newlist.append(newtop)


newlist=sorted(newlist,reverse=True)
for (v,k) in newlist[:10]:
    print(v,k)
