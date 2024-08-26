import requests
import json

from 爬取入门.requesets模块详解 import headers

url = 'https://fanyi.baidu.com/sug'
# headers = {
#     'User-Agent':'Mozilla/5.0'
#     }
words = input('请输入要翻译的内容')
# data = {'kw':words}
# response = requests.post(url,headers=headers,data=data)
# print(response.text)
# result = json.loads(response.text)
# print(result)