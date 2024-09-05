import streamlit as st

st.write('### BMI v1.0')
height = int(st.number_input('请输入你的身高(cm)', 100, 220, 187))
weight = int(st.number_input('请输入你的体重(kg)', 30, 260, 84))
height /= 100
BMI = round(weight / (height ** 2), 2)
button = st.button('BMI计算')
if button:
    st.write(f'您的BMI是{BMI}')
    if BMI <= 18.40:
        st.write('偏瘦')
    elif BMI > 18.40 and BMI < 24:
        st.write('正常')
    elif BMI >= 24  and BMI < 28:
        st.write('过重')
    else:
        st.write('超重')


    import pandas as pd
    data = {
        '分类': ['偏瘦', '正常', '过重', '超重'],
        'BMI范围': ['<= 18.40','18.40~23.99','24~27.99','>=28']
    }
    df = pd.DataFrame(data)
    st.dataframe(df)