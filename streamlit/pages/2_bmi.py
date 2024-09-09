import streamlit as st
import pandas as pd
import numpy as np
import time

# BMI计算
st.write('### BMI v1.0')
height = int(st.number_input('请输入你的身高(cm)', 100, 220, 187))
weight = float(
    st.number_input('请输入你的体重(kg)', 30.0, 260.0, 84.0, 0.1, '%0.1f', help='输入你的体重可以保留一位小数'))
height /= 100
BMI = round(weight / (height ** 2), 2)
button = st.button('BMI计算')
st.caption('BMI计算公式')  # 小号字体
st.code('weight/(height**2)# 体重(kg)/身高(米)²', 'python')
if button:
    st.caption(f'您的BMI是{BMI}')
    if BMI <= 18.40:
        st.write('偏瘦，需要增肥了！')
    elif BMI > 18.40 and BMI < 24:
        st.write('正常，继续保持！')
    elif BMI >= 24 and BMI < 28:
        st.write('过重，该减肥了！')
    else:
        st.write('超重，太该减肥了！')
    st.caption('BMI范围表如下')

    data = {
        '分类': ['偏瘦', '正常', '过重', '超重'],
        'BMI范围': ['<= 18.40', '18.40~23.99', '24~27.99', '>=28']
    }
    df = pd.DataFrame(data)
    st.dataframe(df, width=1000, hide_index=True)
    # 获取当前日期
    current_date = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    # 需要在文件中保存日期/身高/体重/BMI/分类
    # dict_data = dict()
    with open('BMI.txt', 'a') as f:
        f.write(f'{current_date},{height},{weight},{BMI} \n')
    # 日期列表
    data_date = []
    # 身高列表
    data_height = []
    # 体重列表
    data_weight = []
    # BMI列表
    data_BMI = []
    # 分类列表
    # data_classification = []
    with open('BMI.txt', 'r') as f:
        content = f.readlines()
        for i in content:
            # st.write(f'{i}')
            list_content = i.split(',')
            data_date.append(list_content[0])
            data_height.append(float(list_content[1]))
            data_weight.append(float(list_content[2]))
            data_BMI.append(float(list_content[3]))
    data_cla = {
        '日期': data_date,
        '身高(m)': data_height,
        '体重(kg)': data_weight,
        'BMI': data_BMI,
        # 'classification': data_classification
    }
    df1 = pd.DataFrame(data_cla)
    st.dataframe(df1, width=1000, hide_index=True)