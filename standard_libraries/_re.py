import re

text = "Email is test123@gmail.com"
print(re.findall(r"\w+@\w+\.\w+", text))
