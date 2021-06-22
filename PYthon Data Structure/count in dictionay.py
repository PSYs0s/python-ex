count=dict()
names=['toha','toha','safi','tanvir']
for name in names:
    if name not in count:
        count[name]=1
    else:
        count[name]=count[name]+1
print(count)
if name in count:
    x=count[name]
    print('yas')
else:
    x=0
x=count.get('t',0)#get() method for suring is it here or not
print(x)
