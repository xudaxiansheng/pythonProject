# 导入lxml包
import requests
from lxml import etree

url = 'https://www.zhihu.com/question/318800005/answer/2404399358'
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36'
}
response = requests.get(url, headers=headers)
html = etree.HTML(response.text)
html = html.xpath('//span[@class="RichText ztext CopyrightRichText-richText css-1ygg4xu"]/figure')
print(html)
list_pic = []
for pic in html:
    pic_url = pic.xpath('.//img')
    list_pic.append(pic_url)
