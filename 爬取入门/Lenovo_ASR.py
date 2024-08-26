from idlelib.iomenu import encoding

import requests
from urllib.parse import urlencode
import base64

from certifi import contents

base_url = 'https://voice.lenovomm.com/lasf/cloudasr'
headers = {
    # 'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
    'lenovokey':'LENOVO-VOICE-4a817cb58t970d468hc886a',
    'secretkey':'C3BAC3A28F97B6E73840BE8F4DC8DB0F',
    'channel':'cloudasr'
}
with open('voice.mp3','rb') as f:
     voice = f.read()
# text = input('输入要合成的语音文字：')
#      print(voice)
parm = {
    'scene': 'short',
    'language':'chinese',
    'sample':1,
    'audioFormat':'speex_8000_16bit_sample',
    'sessionid':1356663021692,
    'packageid':1,
    'over':1,
    'voice-data':voice
}
# url = base_url + '?' + urlencode(parm)
r = requests.post(base_url,headers=headers,data=parm)
# rel = r.json()
print(r)