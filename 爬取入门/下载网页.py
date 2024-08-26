# 导入requests
import requests
# 变量请求地址，以及请求地址
url = 'https://www.baidu.com/'

headers = {
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36'
}
# 请求网页
response = requests.get(url=url, headers=headers)

# 写入拿到的内容
with open('baidu.html', 'w' , encoding= 'utf-8') as f:
    f.write(response.content.decode())