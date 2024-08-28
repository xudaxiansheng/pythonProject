import requests
import streamlit as st

url = 'https://voice.lenovomm.com/lasf/cloudtts'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
    'lenovoKey': 'LENOVO-VOICE-4a817cb58t970d468hc886a',
    'secretKey': 'C3BAC3A28F97B6E73840BE8F4DC8DB0F',
    'channel': 'cloudasr'
}
st.write('# 语音合成 v1.1')
text = st.text_area('>输入要合成的文字', '举例：我是一只小小小小鸟，想要飞飞飞飞飞飞的更高。')
speed = st.number_input('设置播放的语速:', 0, 9, 5)
volume = st.number_input('设置语音的音量:', 0, 9, 5)
pitch = st.number_input('设置语音的音调:', 0, 9, 5)
speaker = st.radio('设置语音角色', [':rainbow[db4]', 'db2'],captions=['女声','男声'])
button = st.button('合成语音')

data = {
    'text': text,
    'user': 15966882,
    'speed': speed,
    'volume': volume,
    'pitch': pitch,
    'speaker': speaker
}
if button:
    with st.spinner('合成语音中......'):
        r = requests.post(url, headers=headers, data=data)
        with open('voice.mp3', 'wb') as f:
            f.write(r.content)
        st.audio('voice.mp3')


