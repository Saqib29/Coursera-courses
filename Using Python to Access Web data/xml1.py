import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("Enter - ")
uh = urllib.request.urlopen(url, context=ctx)
data = uh.read()



tree = ET.fromstring(data)

for line in tree:
    print(line.findall('comments/comment/count'))

results = tree.findall('comments/comment')
count =0
sum=0
for item in results:
    x = int(item.find('count').text)
    count =count+1
    sum = sum+x

print ("Count : ",count)
print ("Sum : ",sum)
