fhandle=open('mbox-short.txt', 'r')
hourdic=dict()
for line in fhandle:
    if line.startswith('From '):
        words=line.split()
        time=words[5]
        part_of_time=time.split(':')
        hour=part_of_time[0]
        if not hour in hourdic:
            hourdic[hour]=hourdic.get(hour,0)+1
        else:
            hourdic[hour]=hourdic[hour]+1
for (k,v) in sorted(hourdic.items()):
    print(k,v)
