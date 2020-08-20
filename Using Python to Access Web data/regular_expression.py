import re

data = """<p>Please click <a href="http://www.dr-chuck.com">here</a></p>"""


y = re.findall('href="(.+)"', data)
print(y)
