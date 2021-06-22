fhand=open('words.txt')
for line in fhand:
    if line.startswith('W'): #here, we can use -if not line.startswith('w'):
                            #continue. thhen command back top and seaerch again if found nothing
                            #this like a skip section
                            #we can write also this:
                            #if not 'w' in line
    line=line.rstrip()
    print(line)
