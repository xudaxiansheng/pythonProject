from my_package import ASR
import streamlit as st


path = "../streamlit/16k.pcm"  # 请将您的语音文件路径改为本地路径
content = ASR.main(path)
print(content)
st.write("语音识别结果：", content)


file = st.file_uploader("上传语音文件", type=["wav", "mp3"])
if file is not None:
    text = speech_to_text(file)
    st.write(f"识别结果: \n```{text}```")