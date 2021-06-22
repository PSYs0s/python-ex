fhand=open('mbox-short.txt')
for line in fhand:
    line=line.rstrip()
    if line.startswith('From '):
        words=line.split()
        email=words[1]
        part=email.split('@')
        print(words[2],part)
