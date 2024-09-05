import streamlit as st
import speech_recognition as sr

# 初始化recognizer
recognizer = sr.Recognizer()


# 语音识别的函数
def speech_to_text(audio_file):
    with sr.AudioFile(audio_file) as source:
        audio = recognizer.record(source)
    try:
        return recognizer.recognize_google(audio)
    except sr.UnknownValueError:
        st.write('无法理解语音')
    except sr.RequestError as e:
        st.write(f"识别服务出错; {e}")


# 运行streamlit应用程序
st.title('语音识别')
st.write("上传语音文件进行识别或者通过麦克风实时语音识别")

# 选择文件
file = st.file_uploader("上传语音文件", type=["wav", "mp3"])
if file is not None:
    text = speech_to_text(file)
    st.write(f"识别结果: \n```{text}```")

# 实时语音识别
recognize_now = st.button("开始实时语音识别")
if recognize_now:
    with sr.Microphone() as source:
        st.write("请开始说话...")
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio)
            st.write(f"你说了: \n```{text}```")
        except sr.UnknownValueError:
            st.write("无法理解语音")
        except sr.RequestError as e:
            st.write(f"识别服务出错; {e}")