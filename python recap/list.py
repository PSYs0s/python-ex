l=[9,21,34,56,76,8]
#list value changable by index position assign value
l[0]=100
print(l,'\n')
#list can be sliced
print(l[1:3],'\n')

stuff=list()
stuff.append('nice')
stuff.append(34)
print(stuff,'\n')

#checking element is in list or not--->return boolean
print(45 in stuff)

#sorting
l.sort()
print('\n',l)

#split
name='I am toha'
print(name.split())