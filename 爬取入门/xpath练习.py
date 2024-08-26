# 导入lxml包
import requests
from lxml import etree
url = 'https://movie.douban.com/top250'
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36'
}
response = requests.get(url, headers=headers)
html = response.text
html = etree.HTML(html)
# 找到大路径
ol = html.xpath('//ol/li')
for li in ol:
    title = li.xpath('.//span[@class="title"][1]/text()')
    score = li.xpath('.//span[@class="rating_num"][1]/text()')
    print(f'电影名称：{title[0]}，评分：{score[0]}')
