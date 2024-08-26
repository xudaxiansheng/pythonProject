import requests

url = 'https://m701.music.126.net/20240823154815/5c0345d53e4259af6014aa4f11ebadfe/jdyyaac/obj/w5rDlsOJwrLDjj7CmsOj/28481680356/9cef/6518/cfc8/25113cb2c940ddb529b64ecf946ed34f.m4a'
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36'
}

response = requests.get(url, headers=headers)
with open('消愁.m4a', 'wb') as f:
    f.write(response.content)
