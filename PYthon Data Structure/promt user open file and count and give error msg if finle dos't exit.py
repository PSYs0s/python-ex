while(1):
    fname=input('Enter a file name:')
    try:
        fhand=open(fname)
        count=0
    except:
        print('This file dosn not exit. Please enter file name correctly!')
        continue
    for line in fhand:
        line=line.rstrip()
        print(line)
        count=count+1
    print('\nTotal line number:',count)
