import re

f = open(input("Enter file name:"))
text = re.findall(r'[0-9]+', f.read())
num = [int(i) for i in text]
print('Sum:', sum(num))

