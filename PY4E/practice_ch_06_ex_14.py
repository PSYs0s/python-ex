str = "X-DSPAM-Confidence:0.8475"
start=str.find(":")
str_num=float(str[start+1:])
print(str_num)
