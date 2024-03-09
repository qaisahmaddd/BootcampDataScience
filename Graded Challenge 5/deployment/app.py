import streamlit as st

import eda
import prediction

# options = ["HOME", eda, prediction]
page = st.sidebar.selectbox(label="Pilih Menu", options=["HOME", "eda", "prediction"])

# eda.run()
# prediction.run()

if page == 'HOME':
    st.header('Selamat Datang di Model Pertama Qais')
    st.write('#Silahkan Pilih Menu di Samping')

elif page == 'eda':
    eda.run()

else:
    prediction.run()