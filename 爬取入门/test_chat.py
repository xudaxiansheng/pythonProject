import requests
import json

while True:
    print('*************************************')
    a = input('玉米说：')
    url = 'http://api.qingyunke.com/api.php?key=free&appid=0&msg='+ a
    response = requests.get(url)
    res = json.loads(response.text)
    words = str(res['content']).replace('{br}','\n')
    print(f'小白说：{words}')