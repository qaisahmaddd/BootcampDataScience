import streamlit as st
import json, pickle
import pandas as pd

def run():
    st.write("# Ahmad Qais Alfiansyah")
    st.write("## Graded Challenge 5")
    st.write("### Model prediction")
    st.write("Halo, selamat datang. Silahkan input datanya:")

    # Load model
    with open('./model.pkl', 'rb') as file_1:
        modelku = pickle.load(file_1)


    with st.form("Input data"):
        balance = st.number_input('Balance', min_value=0, help="balance")
        gender = st.selectbox('Gender',(0, 1))
        education = st.selectbox('Education',(6,4,1,2,3,5,0))
        marital = st.selectbox('Marital Status',(0,1,2,3))
        age = st.slider('Age', 10, 80, 15)
        pay0 = st.slider('Pay 0', -5, 10, 0)
        pay2 = st.slider('Pay 2', -5, 10, 0)
        pay3 = st.slider('Pay 3', -5, 10, 0)
        pay4 = st.slider('Pay 4', -5, 10, 0)
        pay5 = st.slider('Pay 5', -5, 10, 0)
        pay6 = st.slider('Pay 6', -5, 10, 0)

        submit = st.form_submit_button('Submit')

    data_predict = {
        "limit_balance":balance,
        "sex":gender,
        "education_level":education,
        "marital_status":marital,
        "age":age,
        "pay_0":pay0,
        "pay_2":pay2,
        "pay_3":pay3,
        "pay_4":pay4,
        "pay_5":pay5,
        "pay_6":pay6
    }

    data = pd.DataFrame(data_predict, index=[0])

    st.write("Data : ")
    st.dataframe(data)

    if submit:
        y_pred = modelku.predict(data)
        st.write("Result : ", y_pred)

if __name__ == '__main__':
    run()