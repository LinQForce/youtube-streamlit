from pandas.core.frame import DataFrame
import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title('Streamlit と　Python')

st.write('フレマアップワークス　ライセスン')




option = st.selectbox(
    'ご希望のライセンスを月額版、年額版のどちらかで選択ください。'
    ('月額版','年額版','永久ライセンス')
)
option,'はこちらになります。'
git
condition = st.slider('あばたの調子は？',0,100,50)
'コンディション = ',condition


option = st.radio("ご希望のライセンス",('月額版', '年額版', '永久ライセンス'))
option,'はこちらになります。'


##条件付きチェックBOX  

if st.checkbox('Show Image'):
    img = Image.open('sample.png')
    img2= Image.open(('sample_resize.png'))
    left_column, right_column = st.columns(2)
    left_column.image(img, caption='Ange', width=350)
    right_column.image(img2, caption='Charlot', width=350)