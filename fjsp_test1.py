import streamlit as st
import pandas as pd
import numpy as np
from fjsp_Q import *




# Display editor's content as you type


st.header('FJSP_DEMO')

with st.sidebar:
    selecop = st.selectbox(
    '설정 메뉴',
    ('job.csv', 'setup.csv', 'sim.csv'))

    if selecop == 'job.csv':
        st.subheader('job.csv파일 생성 설정')

        number = st.number_input('job의 갯수')
        number = int(number)
        value1,value2 = st.slider('job타입의 난수범위',0,100,(1,10))
        st.write('선택범위', value1,value2)

        if st.button('job.csv생성'):
            job(number,value1,value2)
            st.write('생성완료')

    elif selecop == 'setup.csv':
        st.subheader('set.csv파일 생성 설정')

        value3,value4 = st.slider(
        'setup시간 난수의 범위',0,100,(1,10))
        st.write('선택범위', value3,value4)

        if st.button('setup.csv생성'):
            setup(value3,value4)

    elif selecop == 'sim.csv':
        st.subheader('sim.csv파일 생성 설정')

        number2 = st.number_input('기계의 갯수')
        number2 = int(number2)
        value5,value6 = st.slider('processtime의 난수범위',0,100,(1,10))
        st.write('선택범위', value5,value6)

        value7,value8 = st.slider(
    'job_operation의 난수범위',
    0,100,(1,10))
        st.write('선택범위', value7,value8)

        if st.button('sim.csv생성'):
            sim(number2,value5,value6,value7,value8)


job_df = pd.read_csv('FJSP_Job.csv', index_col=False)
setup_df = pd.read_csv('FJSP_Set.csv', index_col=False)
sim_df = pd.read_csv('FJSP_Sim.csv', index_col=False)

option = st.selectbox(
    '선택할 데이터셋?',('job.csv', 'setup.csv', 'sim.csv'))
if st.button('데이터 보기'):
    st.subheader('데이터셋')
    st.write('You selected:', option)

    if option == 'job.csv':
        st.write(job_df)
    elif option == 'setup.csv':
        st.write(setup_df)
    elif option == 'sim.csv':
        st.write(sim_df)

