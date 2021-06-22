import math
import random

decibles=10*math.log10(100)
radians=0.7
height=math.sin(radians)
deg=45
rad=deg/360*2*math.pi
res=math.sin(rad)
print(height)
print(rad)
print(res)
print(decibles)

print(math.sqrt(2),'\n')

for i in range(10):
    x=random.random()
    print(x)
print('\n')
print(random.randint(5,10))
print('\n')
num=[1,2,3,4,5,6]
print(random.choice(num))#choice using in sequensital selecting