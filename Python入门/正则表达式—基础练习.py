import re
s = 'python is encode python'
# result = re.match('python',s)
# print(result)
# print(result.span())

# result = re.search('python',s)
# print(result)
# print(result.span())
result = re.findall('python', s)
print(result)
print(result.count('python'))