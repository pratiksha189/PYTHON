import re
# massage=" morning good have a nice day"
# match=bool(re.search(r'good',massage))
# print(match)
# match=re.search(r'good',massage)
# if match:
#     print(match.span())
#     print(match.group())
# else:
#     print("no match")
#
# print(re.findall(r"good",massage))
words="sit wit chit that bir fat pit it fit unit"
print(bool(re.search(r'^sit',words)))
print(bool(re.search(r't$',words)))

pattern=r'\b[a-z]*it\b'
print(re.findall(pattern,words))

pattern=r'\b[a-z]+it\b'
print(re.findall(pattern,words))

pattern=r'\b[a-z]?it\b'
print(re.findall(pattern,words))

pattern=r'\b\w{1}it\b'
print(re.findall(pattern,words))

