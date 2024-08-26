"""
1.创建一个爬取类
a.构造方法去接受默认的参数：url
2.创建获取URL方法，每页25条，遍历出10个页面地址，生成一个list列表
3.拿到页面去遍历出每个页面的电影名称和评分

"""
import requests
from lxml import etree

from 爬取入门.下载单个音乐 import headers


class Doban:
    def __init__(self,url):
        self.url=url

    def List_data(self):
        list_url=[] #创建空列表去承载后续的页面地址
        for i in range(10):
            url = self.url + f'?start={i*25}&filter='
            list_url.append(url)  # 追加URL列表
        return list_url

    def read_data(self):
        list_url=self.List_data()
        i = 0
        for url in list_url:
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36'
            }
            response = requests.get(url=url, headers=headers)
            html = response.text
            html = etree.HTML(html)
            li_list = html.xpath('//ol/li')
            for li in li_list:
                title = li.xpath('.//span[@class="title"][1]/text()')
                score = li.xpath('.//span[@class="rating_num"][1]/text()')
                i +=  1
                print(f'豆瓣评分第{i}名，\t电影名称是：{title[0]}\t\t\t\t评分是：{score[0]}')





if __name__ == '__main__':
    doban = Doban(url="https://movie.douban.com/top250")
    doban.read_data()
