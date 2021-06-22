text = "X-DSPAM-Confidence:    0.8475";
fnumber=text.find('0')
host=text[fnumber:]
float(host)
print(host)
