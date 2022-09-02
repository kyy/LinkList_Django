import re

regex = r'(https?://[^\"\s>]+)'

test_str = ("Hello, https://getbootstrap.ru/docs/v4-alpha/content/tables/ pythonworld.ru!\n"
            "Checking https://гто.рф\n"
            "http://microsoft.com")

matches = re.finditer(regex, test_str, re.MULTILINE)
a=[]
for match in matches:
    a.append(match.group())
print(a)
