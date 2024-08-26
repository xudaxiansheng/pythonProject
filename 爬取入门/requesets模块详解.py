"""
Python-requests 模块详解
1.模块说明
requests 是使用Apache2 licensed 许可证的HTTP库
用PYthon编写。
比urlli2模块更简洁
Requests 支持HTTP连接保持和连接池，支持使用cookie保持会话，支持文件上传，支持自动响应内容的编码，支持国际化的URL和post数据自动编码。
在Python内置模块的基础上进行了高度的封装，从而使得Python进行网络请求时，变得人性化使用requests可以轻而易举的完成浏览器可有的任何操作。
现代、国际化、友好。
requests会自动实现持久连接Keep-alive
"""

# 2.基础入门
# 1）导入模块
# import requests

# 2)发送请求的简洁
# 实例代码：获取一个网页（个人github)
import requests
r =  requests.get('https://github.com/Ranxf')   # 最基本的不带参数的get请求
r1 = requests.get(url ='http://dict.baidu.com/s',params={'wd':'python'})    #带参数的get请求
print(r.text)

# 我们就可以使用该方式使用以下各种方法
requests.get('https://github.com/timeline.json')    # GET请求
requests.post('http://httppin.org/post')            # POST请求
requests.put('http://httppin.org/put')              # PUT请求
requests.delete('http://httppin.org/delete')        # DELETE请求
requests.head('http://httppin.org/head')            # HEAD请求
requests.options('http://httppin.org/')             # OPTIONS请求


# 3)为url传递参数
url_parmas ={'key':'valus'}                         # 字典传递参数，如果值为None的键不对被添加到URL中
r = requests.get('url',params=url_parmas)
print(r.url)

# 4)响应的内容
r.encoding                                          # 获取当前编码
r.encoding = 'utf-8'                                # 设置编码
r.text                                              # 以encoding解析返回内容，字符串方式的响应体，会自动根据响应头部的字符编码进行解码。
r.content                                           # 以字节形式（二进制）返回，字节方式的响应体，会自动为你解码 gzip和deflate压缩。
r.headers                                           # 以字典对象存储服务器响应头，但是这个字典比较特殊，字典键不区分大小写，若键不存在则返回None。
r.status_code                                       # 响应状态码
r.raw                                               # 返回原始响应体，也就是urllib的response对象，使用r.raw.read().
r.ok                                                # 查看r.ok的布尔值便可以知道是否登陆成功。
# 特殊方法
r.json()                                            # Requests中内置的JSON解码器，以JSON形式返回，前提返回的内容确保是JSON格式的，不然解析出错会抛异常。
r.raise_for_status()                                # 失败请求（非200响应）抛出异常。
# post发送JSON请求
import requests
import json
r = requests.post('https://api.github.com/some/endpoint',data=json.dumps({'some':'data'}))
print(r.json())

# 5)定制头和cookie信息
headers ={'user-agent':'my-app/0.0.1'}
cookie = {'key':'value'}
r = requests.get('url',headers=headers,cookies=cookie)

data = {'some':'data'}
headers ={
    'content-type':'application/json',
    'User-Agent':'Mozilla/5.0 (xll;Ubuntu;Linux x86_64;rv:22.0) Gecko/20100101 Firefox/22.0'
          }
r = requests.post('https://api.github.com/some/endpoint',data=data,headers=headers)
print(r.text)

# 6)响应状态码
# 使用requests方法后，会返回一个response对象，其存储了服务器响应的内容，如上实例中已经提到的r.text、r.status_code......
# 获取文本方式的响应体实例：当你访问r.text之时，会使用其响应的文本编码进行解码，并且你可以修改其编码让t.test使用自定义的编码进行解码。
r = requests.get('http://www.baidu.com')
print(r.text,'\n{}\n'.format('*'*79),r.encoding)
r.encoding = 'GBK'
print(r.text,'\n{}\n'.format('*'*79),r.encoding)

# 示例代码：
import requests
r = requests.get('http://www.baidu.com')            # 最基本的不带参数的get请求
print(r.status_code)
r1 = requests.get('http://dict.baidu.com/s',params={'wd':'python'}) #带参数的get请求
print(r1.url)
print(r1.text)     #打印解码后的返回数据（字符串）

# r.status_code 如果不是200，可以使用r.raise_for_status()抛出异常

# 7）响应
r.headers                                           # 返回字典类型，头信息
r.requests.headers                                  # 返回发送到服务器的头信息
r.cookies                                           # 返回cookie
r.history                                           # 返回重定向信息，当然可以在请求时加上allow_redirect = false 组织重定向

# 8) 超时
r = requests.get('http://www.baidu.com',timeout=1)   # 设置秒数超时，进对于连接有效

# 9）会话对象，能够夸请求保持某些参数
s = requests.Session()
s.auth = ('auth','password')
s.headers = {'key':'value'}
r = s.get('http://www.baidu.com')
r1 = s.get('http://www.baidu.com')

# 10)代理
proxies = {'http':'ip1','https':'ip2'}
requests.get('url',proxies=proxies)

# 汇总：
# HTTP请求类型
# GET类型