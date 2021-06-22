def score(a):
    if a >= 0.9:
        grade="A"
    elif a >= 0.8:
        grade="B"
    elif a >= 0.7:
        grade="C"
    elif a >= 0.6:
        grade="D"
    elif a < 0.6:
        grade="F"
    return grade
inp=input("Score>>")
try:
    value=float(inp)
    grade=score(value)
    print(f"His grade is:{grade}")
except:
    print("Bad input")
