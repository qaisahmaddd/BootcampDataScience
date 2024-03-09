import streamlit as st

import eda
# import prediction

# options = ["HOME", eda, prediction]
page = st.sidebar.selectbox(label="Pilih Menu", options=["HOME", "EDA", "PREDICTION"])


if page == 'HOME':
    st.header('Selamat Datang')
    st.subheader('Ini adalah Tugas NLP GC7 saya:')
    st.subheader('Ahmad Qais')
    st.write('<--- Silahkan Pilih Menu di Samping')

elif page == 'EDA':
    eda.run()

# elif page == 'PREDICTION':
#     prediction.run()

else:
    pass