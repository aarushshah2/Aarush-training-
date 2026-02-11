import re

text = "Contact us at support@example.com"
# re.search() - Find first match
match = re.search(r'\w+@\w+\.\w+', text)
print(match.group() if match else "No match")

# re.findall() - Find all matches
print(re.findall(r'\w+', text))

# re.sub() - Replace patterns
print(re.sub(r'\s', '-', text)) # Replace spaces with dashes