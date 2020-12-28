import re

pattern = re.compile(r'\d\d\d[-]\d\d\d[-]\d\d\d\d')

with open('src/regexp/data.txt', 'r') as f:
    contents = f.read()
    matches = pattern.finditer(contents)

    for match in matches:
        print(match)