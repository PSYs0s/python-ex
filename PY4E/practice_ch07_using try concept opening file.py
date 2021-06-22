fname=input("Enter file name:")
try:
    fhand=open(fname)
except:
    print("Error file name!")
    exit()
count=0
for line in fhand:
    if line.startswith("From: "):
        count=count+1
print(count)
