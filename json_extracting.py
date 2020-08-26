import urllib.request, urllib.parse, urllib.error
import json

url = input('Enter web address: ')
print('Retrieving', url)
uh = urllib.request.urlopen(url)
data =  uh.read().decode()

print("Retrieved:", len(data), "characters")

jf = json.loads(data)
# test print(jf)
print("Comment counts:", len(jf["comments"]))

sum = 0

for each in jf["comments"]:
    sum += each["count"]
print("Sum of all comment counts:", sum)
