#file objects
f=open("file.txt", "r")
fhand=f.read()
print(fhand)
print(f.name)
print(f.mode)
f.close()
#context manager
with open("file.txt", "r") as f:
     f_contents=f.readline()
     print(f_contents)
#differentn for readlines
with open("file.txt", "r") as f:
     f_contents=f.readlines()
     print(f_contents)
print("\n")
#for loop in reading mode
with open("file.txt", "r") as f:
     for line in f:
         line=line.rstrip()
         print(line,end="  ")
print("\n")
#arguments in readn option
with open("file.txt", "r") as f:
    f_contents=f.read(51)
    print(f_contents)

    f_contents=f.read(52)
    print(f_contents)

    f_contents=f.read(51) #if completed then doesnt print
    print(f_contents)
#using variable for argument in read option
with open("file.txt", "r") as f:
    sized=100
    f_file=f.read(sized)
    while len(f_file)>0:
        print(f_file,end="")
        f_file=f.read(sized)

print("\n")
#whats going on in while looping
with open("file.txt", "r") as f:
    sized=10
    f_file=f.read(sized)
    print(f_file,end="")
    #f.seek(0) #it is used for starting beggining same time
    f_file=f.read(sized)
    print(f_file)
    #print(f.tell()) it says us whta is our position.
