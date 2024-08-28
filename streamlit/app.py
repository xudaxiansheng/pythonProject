import streamlit as st
import time

# 登录页面练习

def login(name, psw):
    time.sleep(2)
    return name == 'xu' and psw == '123'


name = st.text_input('name', 'xu')
psw = st.text_input('password', '123')

button = st.button('login')
if button:
    with st.spinner('登录中......'):
        rel = login(name, psw)
        if rel:
            st.write('登录成功')
        else:
            st.write('失败')
