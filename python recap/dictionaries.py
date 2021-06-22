numToWord=dict()
print(numToWord)

#ading items
numToWord={'2':'two','3':'three','4':'four'}
numToWord['1']='one'
print(numToWord)
print(numToWord['3'])
print(len(numToWord))#supports len function

#supports in & always return true if key item available.value item always return false
print('1' in numToWord)
print('one' in numToWord) 

#values method return the value as a list
val=numToWord.values()
print(val)#this list support in method and return true
print('one' in val)

#get method take key & default value and return value
print(numToWord.get('2',0))

#looping
for key in numToWord:
    print(key,numToWord[key])
    
#making sorted\
lst=list(numToWord.keys())
lst.sort()
for key in lst:
    print(key,numToWord[key])