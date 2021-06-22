def countLetter(sen):
    count=0
    for letter in sen:
        count=count+1
    return count
inp=input('Enter a sentence>>')
result=countLetter(inp)
print(result)