a="toha"
b=a[0]
print(b)
print(len(a))
last=a[len(a)-1]
print(last)
print(a[-1])
print(a[-2])
print(a[-3])
print(a[-4])
print("\n")
#tarvel in string
index=0
while index<len(a):
    letter=a[index]
    print(letter)
    index=index+1
print("\n")

for char in a:
    print(char)
#string slice
sen="you are so bad guy"
print(sen[0:5])#including first but excluding last
print(sen[5:9])
print(sen[:5])
print(sen[5:])
#if first index is greater then secound or equal then string will be empty
print("\n")
print(sen[6:5])
print(sen[5:5])
#if no index then print everything
print(sen[:])

#string doesn't support item assignment
'''sen[1]="h"
print(sen[1])'''

#concatenates in string.by this option wee can make new string
greeting="Hello World"
new_greeting="J"+greeting[1:]
print(f"\n{new_greeting}")

#looping counting
word="I am lovely person"
count=0
for letter in word:
    if letter == "e":
        count=count+1
print(count)

#the in oparetor
print("a" in word)

#string comparison
words="bananas"
if words < "banana":
    print("Your word," + words + ", comes before banana.")
elif words > "banana":
    print("Your word," + words + ", comes after banana.")
else:
    print("All right, bananas.")

#string method
print(dir(words))
help(str.capitalize)
print(words.upper())
print(words.lower())
print(words.capitalize())

"""there is a string method named find that searches for the position
of one string within another"""
print(words.find("a"))

#It can take as a second argument the index where it should start
letter="ooaahhdg"
print(letter.find("dg",4))

"""One common task is to remove white space (spaces, tabs, or newlines) from the
beginning and end of a string using the strip method"""
greet="     Hi, I'm Mohammad Toha  "
print(greet)
print(greet.strip())

#Some methods such as startswith return boolean values
print(greet.startswith("     Hi"))

print(greet.lower().strip().startswith("hi"))

#parsing string
data="From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008"
start=data.find("@")
print(start)
finish=data.find(" ",start)
print(finish)
target_part=data[start+1:finish]
print(target_part)

#formating stirng
camels=42
print("%d"%camels)
print("I have %d numbers camels"%camels)
print("For %d years, i have %g number of land and this %s"%(3,1.5,"house"))
