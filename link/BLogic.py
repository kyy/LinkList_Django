import re

# Parsing true format URLS without gabage:
def URL_parser(self):
    regex = r'(https?://[^\"\s>]+)'
    matches = re.finditer(regex, self, re.MULTILINE)
    url_dict = []
    i = 0
    for match in matches:
        i += 1
        url_dict.append(match.group())
    return url_dict, i
