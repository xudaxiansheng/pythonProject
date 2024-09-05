import base64
import urllib
import requests
import json
import streamlit as st

API_KEY = "h4uFI2bziINgwiGA3f4HOuXt"
SECRET_KEY = "uLj2JhalZ4XXuk70zgVvb2M8CCrtwGZz"


def main(path):
    url = "https://vop.baidu.com/server_api"
    speech, length = get_file_content_as_base64(path)
    # speech 可以通过 get_file_content_as_base64("C:\fakepath\16k.wav",False) 方法获取
    payload = json.dumps({
        "format": "pcm",
        "rate": 16000,
        "channel": 1,
        "cuid": "JuipwUUBa356isSBh9JH9mDFaAcgP3x9",
        'speech': speech,
        "len": length,
        "token": get_access_token()
    })
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    r=response.text
    # print(r)
    dict_r = json.loads(r)
    # print(dict_r['result'][0])

    return dict_r['result'][0]

def get_file_content_as_base64(path):
    """
    获取文件base64编码
    :param path: 文件路径
    :param urlencoded: 是否对结果进行urlencoded
    :return: base64编码信息
    """
    with open(path, "rb") as f:
        res = f.read()
        length = len(res)
        speech = base64.b64encode(res)
        speech = str(speech, 'utf-8')
    return speech, length


def get_access_token():
    """
    使用 AK，SK 生成鉴权签名（Access Token）
    :return: access_token，或是None(如果错误)
    """
    url = "https://aip.baidubce.com/oauth/2.0/token"
    params = {"grant_type": "client_credentials", "client_id": API_KEY, "client_secret": SECRET_KEY}
    return str(requests.post(url, params=params).json().get("access_token"))


if __name__ == '__main__':
    path = "../streamlit/16k.pcm"  # 请将您的语音文件路径改为本地路径
    content = main(path)
    print(content)
