import streamlit as st
import requests
import json

st.markdown('#welcome to my chat!')
st.caption(
    '请输入你要了解的内容：歌词后来/笑话/成语一生一世/翻译i love you'
           )
a = st.text_input('')
if a:
    url = 'http://api.qingyunke.com/api.php?key=free&appid=0&msg=' + a
    response = requests.get(url)
    res = json.loads(response.text)
    # words = res['content']
    # words = str(res['content']).replace('{br}','\n')
    words = res['content'].split('{br}')
    for i in words:
        i = i + '\n'
        st.write(i)
    # st.write(f'通天教主：{words}')
    # print(f'小白说：{words}')
