import requests
import base64
url = 'https://voice.lenovomm.com/lasf/cloudtts'
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
    'lenovoKey':'LENOVO-VOICE-4a817cb58t970d468hc886a',
    'secretKey':'C3BAC3A28F97B6E73840BE8F4DC8DB0F',
    'channel':'cloudasr'
}
# with open('滕王阁序.txt','r',encoding='utf-8') as f:
#     text = f.read()
text = input('输入要合成的语音文字：')
try:
    speed = int(input('设置播放的语速，在0~9之间，默认为5:'))
except:
    speed = 5
try:
    volume = int(input('设置语音的音量，在0~9之间，默认为5:'))
except:
    volume = 5
try:
    pitch = int(input('设置语音的音调，在0~9之间，默认为5中音调:'))
except:
    pitch = 5
try:
    speaker = input('db4：女声 db2：男生;默认为：db4:')
except:
    speaker = 'db4'

data = {
    'text': text,
    'user':15966882,
    'speed':speed,
    'volume':volume,
    'pitch':pitch,
    'audioType':'wav',
    'speaker':speaker
}
r = requests.post(url, headers=headers, data=data)
with open('../streamlit/voice.wav', 'wb') as f:
    f.write(r.content)