import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
def run():
    st.title('Exploratory Data Analytics')
    st.write('## Ahmad Qais Alfiansyah')
    st.write("### Graded Challenge 5")

    # Load Data
    st.markdown("<h2 style='text-align:center;'>Gambaran Dataset</h2>", unsafe_allow_html=True)
    df= pd.read_csv('../P1G5_Set_1_ahmad_qais.csv')
    st.dataframe(df)

    int_col= df.select_dtypes(include= ['int'])
    flt_col= df.select_dtypes(exclude= ['int'])

    a = int_col.nunique()
    b = flt_col.nunique()

    fig= plt.figure(figsize=(12, 5))
    plt.subplot(1, 2, 1)
    bars1 = plt.barh(int_col.columns, a, color='#1D3D71')  # Menggunakan columns dari int_col sebagai label sumbu y
    plt.title('Number of Unique Values (Categorical Columns)')
    plt.xlabel('Number of Unique Values')
    plt.ylabel('Column Names')

    st.markdown("<h2 style='text-align:center;'>Jumlah Unique Value</h2>", unsafe_allow_html=True)
    # Menambahkan nilai y pada grafik batang
    for bar, count in zip(bars1, a):
        plt.text(count, bar.get_y() + bar.get_height() / 2, str(count), va='center')

    plt.subplot(1, 2, 2)
    bars2 = plt.barh(flt_col.columns, b, color='#F26634')  # Menggunakan columns dari flt_col sebagai label sumbu y
    plt.title('Number of Unique Values (Numeric Columns)')
    plt.xlabel('Number of Unique Values')
    plt.ylabel('Column Names')

    # Menambahkan nilai y pada grafik batang
    for bar, count in zip(bars2, b):
        plt.text(count, bar.get_y() + bar.get_height() / 2, str(count), va='center')

    plt.tight_layout()
    # plt.show()
    st.pyplot(fig)


    st.markdown("<h2 style='text-align:center;'>Distribusi Data Kolom Tipe Interger (Kategorikal)</h2>", unsafe_allow_html=True)

    cols = len(int_col.columns)
    fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(12, cols * 1))
    axes = axes.flatten()  

    for i, kolom in enumerate(int_col.columns):
        ax = sns.countplot(data=int_col, x=kolom, color= '#1D3D71', ax=axes[i])
        ax.set_title(f'Distribusi Data {kolom}')
        ax.set_xlabel(kolom)
        # ax.set_xticklabels(ax.get_xticklabels(), rotation= 90)

    plt.tight_layout()
    st.pyplot(fig)

    st.markdown("<h2 style='text-align:center;'>Distribusi Data Tipe Kolom Float (Numerikal)</h2>", unsafe_allow_html=True)
    cols = len(flt_col.columns)
    fig, axes = plt.subplots(nrows=7, ncols=3, figsize=(18, 5 * 4)) 
    axes = axes.flatten()

    for i, kolom in enumerate(flt_col.columns):
        ax = sns.histplot(data=flt_col, x=kolom, color='#F26634', bins=30, ax=axes[i])
        ax.set_title(f'Distribusi Data {kolom}')
        ax.set_xlabel(kolom)

    plt.tight_layout()
    st.pyplot(fig)

    st.markdown("<h2 style='text-align:center;'>Limit Balance Berdasarkan Default Payment</h2>", unsafe_allow_html=True)

    fig= plt.figure(figsize=(4,3))
    # ax = sns.histplot(data=flt_col, x=kolom, color='#F26634', bins=30, ax=axes[i])
    ax= sns.barplot(data=df, x='default_payment_next_month', y='limit_balance', color='#F26634')
    plt.xlabel('Default Payment Next Month')
    plt.ylabel('Limit Balance')
    plt.title('Limit Balance Berdasarkan Default Payment')
    plt.legend()
    st.pyplot(fig)

    st.markdown("<h2 style='text-align:center;'>Distribusi Default Payment Berdasarkan Education Level</h2>", unsafe_allow_html=True)

    fig= plt.figure(figsize=(4,3))
    # ax = sns.histplot(data=flt_col, x=kolom, color='#F26634', bins=30, ax=axes[i])
    ax= sns.barplot(data=df, x='education_level', y='default_payment_next_month', color='#F26634')
    plt.xlabel('Education Level')
    plt.ylabel('Default Payment Next Month')
    plt.legend()
    st.pyplot(fig)

    st.markdown("<h2 style='text-align:center;'>Data Ouliers</h2>", unsafe_allow_html=True)

    for i in range(0, 20, 3):
        cols = flt_col.columns[i:i+3] 

        # Create a figure with 3 subplots
        fig, axs = plt.subplots(1, 3, figsize=(12, 3))

        for j, kolom in enumerate(cols):
            sns.boxplot(x=flt_col[kolom], ax=axs[j], color='#F26634')
            axs[j].set_facecolor('white')
            axs[j].set_title(f'Boxplot of {kolom}', color='#1D3D71')
            axs[j].set_xlabel(kolom, color='#1D3D71')
            axs[j].set_ylabel('Values', color='#1D3D71')
            axs[j].tick_params(colors='#1D3D71')

        plt.tight_layout()
        st.pyplot(fig)

    st.markdown("<h2 style='text-align:center;'>Cek Data Imbalance</h2>", unsafe_allow_html=True)

    fig= plt.figure(figsize=(3, 4))
    ax = sns.countplot(data=df, x='default_payment_next_month', color='#F26634')

    for p in ax.patches:
        ax.annotate(f'{p.get_height()}', (p.get_x() + p.get_width() / 2, p.get_height()), ha='center', va='bottom')

    plt.xlabel('Default Payment Next Month')
    plt.ylabel('Counts')
    plt.tight_layout()
    st.pyplot(fig)

if __name__ == '__main__':
    run()