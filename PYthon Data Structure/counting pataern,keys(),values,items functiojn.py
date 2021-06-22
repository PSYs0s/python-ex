count=dict()
print('Enter a text line below!')
line=input('>')
words=line.split()
print('Words:',words)
print('counting......')
for word in words:
    count[word]=count.get(word,0)+1
print('Counts:',count)

for key in count:#definite loop and dictionaries
    print(key,count[key])

print(list(count))
print(count.keys())
print(count.values())
print(count.items())

for key,key_value in count.items():
    print(key,key_value)
