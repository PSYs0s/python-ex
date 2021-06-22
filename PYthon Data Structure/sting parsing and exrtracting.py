data='From come toha.bdalo@gmail.com SAT UTC 6.60am'
startp=data.find('@')
print(startp)
finishsp=data.find(' ',startp)
print(finishsp)
host=data[startp+1:finishsp]
print(host)
