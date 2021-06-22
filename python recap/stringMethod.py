stuff='Hello World     '
print(stuff.capitalize())
print(stuff.upper())
print(stuff.lower())
print('\n')

#find index method
print(stuff.find('o',6))#sec parameter indicate where should start searching

#strip method-remove white space
print(stuff.strip())

#startswith method- return true if line start exactly word
print(stuff.startswith('Hello'))

#parsing string
data='From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
atpos=data.find('@')
sppos=data.find(' ',atpos)
print(sppos)
host=data[atpos+1:sppos]
print(host)
