fname=input(">>")
fhand=open(fname)
count=0
another_count=0
for line in fhand:
    if line.startswith("From: "):
        count=count+1
print(count)
