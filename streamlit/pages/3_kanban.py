import streamlit as st
import pandas as pd
import numpy as np

# 创建示例数据
np.random.seed(0)
data = pd.DataFrame(np.random.randn(100, 3), columns=['A', 'B', 'C'])

# 设置页面标题
st.title('Streamlit 可视化示例')

# 选择数据列
selection = st.sidebar.multiselect('选择列', data.columns, default=['A', 'B'])

# 绘制折线图
chart_data = data[selection]
st.line_chart(chart_data)