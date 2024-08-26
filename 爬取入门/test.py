# import requests
# import json
# url = 'https://fanyi.baidu.com/sug'
# headers = {
#     'User-Agent':'Mozilla/5.0'
#     }
# words = input('请输入要翻译的内容')
# data = {'kw':words}
# response = requests.post(url,headers=headers,data=data)
# # print(response.text)
# result = response.json()
# # result = json.loads(response.text)
# for i in result['data']:
#     print(i['v'])
words = int(input('请输入'))
print(type(words))
print(words)