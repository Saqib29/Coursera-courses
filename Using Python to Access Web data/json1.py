import urllib.request, urllib.parse, urllib.error
import json
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("Enter Url: ")
data = urllib.request.urlopen(url, context=ctx)
info = json.load(data)
print(json.dumps(info, indent=4))
sum = 0

for line in info['comments']:
    sum += line['count']


print("Sum: ", sum)


# http://py4e-data.dr-chuck.net/comments_748916.json
# http://py4e-data.dr-chuck.net/comments_42.json
