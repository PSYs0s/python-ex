#indexing
name="toha"
print(name[0])
#length
print('\n',len(name),'\n')

#traversing through string
index=0
while index<len(name):
    print(name[index])
    index=index+1

ind=len(name)
print('\n')
while ind>0:
    print(name[ind-1])
    ind=ind-1
    
#string slice
s= 'I am toha'
print(s[0:5])
print(s[:5])
print(s[6:])
print(s[5:5])#if first index is equal or greater than second , result will be emptyy string
print(s[:])#take full string
#-->s[0]='J' not ok
#string are not changable by assigning value in index wise but we can follow this
new_Str='Hi,'+ s[:] #we can use it to replace nidex values[1:]
print(new_Str)

#in operator take true str and return true if first str is a sub str of secound
print(s in new_Str)

#format operaor convert string
number=10
english=78.7
bangla='bangla'
print('I got %d number in the exam' %number,'in english i got %g'%english,'In %s i got 25'%bangla)