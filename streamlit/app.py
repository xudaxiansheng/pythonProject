from my_package import ASR
import streamlit as st


path = "../streamlit/16k.pcm"  # 请将您的语音文件路径改为本地路径
content = ASR.main(path)
print(content)
st.write("语音识别结果：", content)