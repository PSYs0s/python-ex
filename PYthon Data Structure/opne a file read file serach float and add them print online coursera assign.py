fname=input('Enter a file name: ')
fhand=open(fname)
tsum=0
count=0
for line in fhand:
    if line.startswith('X-DSPAM-Confidence:'):
        startp=line.find(':')
        store_value=line[startp+1:]
        fstore=float(store_value)
        tsum=tsum+fstore
        count=count+1
        print(line)
print(tsum/count)
