fhand=open('mbox-short.txt', 'r')
count=dict()
for line in fhand:
    if line.startswith('From '):#check 'From word'
        word=line.split()
        name=word[1]#filter option
        if not name in count:#storing process in dictionary
            count[name]=count.get(name, 0)+1
        else:
            count[name]=count[name]+1
#finding name who send email more than other
bigcount=None
bigname=None
for key,value in count.items():
    if bigcount is None or value > bigcount:
        bigcount=value
        bigname=key
print(bigname,bigcount)
#sorted dictionary not use sort() function
print(sorted(count.items()))
