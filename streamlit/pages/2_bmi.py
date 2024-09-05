import streamlit as st

st.write('### BMI v1.0')
height = int(st.number_input('请输入你的身高(cm)', 100, 220, 187))
weight = int(st.number_input('请输入你的体重(kg)', 30, 260, 84))
height /=100
BMI = round( weight/(height**2),2)
st.write(f'您的BMI是{BMI}')
