import wave
from tkinter.constants import PROJECTING
from urllib.parse import urlencode
import requests
import json




base_url = 'https://voice.lenovomm.com/lasf/cloudasr'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
    'lenovoKey': 'LENOVO-VOICE-4a817cb58t970d468hc886a',
    'secretKey': 'C3BAC3A28F97B6E73840BE8F4DC8DB0F',
    'channel': 'cloudasr'
}
with open('../streamlit/16k.pcm', 'rb') as f:
    byte_vo = f.read()
    byte_array =bytearray(byte_vo)

data = {
    'scene': 'short',
    'audioFormat': 'pcm_16000_16bit_sample',
    'sessionid': 1356663021692,
    'packageid': 1,
    'over': 1,
    'voice-data': byte_array
}
# data_new = urlencode(data)
# parmas = {
#     'param-data': data_new,
#     'voice-data': byte_array
# }
r= requests.post(base_url, headers=headers, data=data)
code = r.status_code
print(code)
r = json.loads(r.text)
print(r)
print(r['allDur'])
