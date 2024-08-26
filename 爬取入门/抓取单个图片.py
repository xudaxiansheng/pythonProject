# 导入requests
import requests
# 变量请求地址，以及请求地址
url = 'https://picx.zhimg.com/70/v2-8e79f86ef1088be222056c5182ed307a_1440w.avis?source=172ae18b&biz_tag=Post'

headers = {
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36'
}
# 请求网页
response = requests.get(url=url, headers=headers)

# 写入拿到的内容
with open('壁纸.png', 'wb') as f:
    f.write(response.content)