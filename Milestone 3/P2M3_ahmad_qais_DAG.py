'''
=================================================
Milestone 3

Nama  : Ahmad Qais Alfiansyah
Batch : FTDS-027-RMT

Program ini dibuat untuk melakukan automatisasi transform dan load data dari PostgreSQL ke ElasticSearch.
Adapun dataset yang dipakai adalah dataset mengenai Transaksi perusahaan Superstore.  
Program diinstruksikan ke berbagai tugas seperti membaca file dari sql, bersihkan data, dan load to Elastic Search
Data Clean dari sini juga akan digunakan oleh script Gread Validation di file terpisah
=================================================
'''
import pandas as pd

import psycopg2 as db

from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
from elasticsearch import Elasticsearch
import datetime as dt
from datetime import timedelta


conn_string="dbname='airflow' host='postgres' user='airflow' password='airflow' port= 5432"
conn=db.connect(conn_string)

# Membuat Pandas DataFrame dari data tersebut
df=pd.read_sql("select * from table_m3", conn)
'''
Dalam fungsi clean_data ini saya akan mendefinisikan:
1. Hapus data yang duplikat (Jika ada)
2. Normalisasi nama kolom:
    - Semua nama kolom menjadi lowercase
    - Mengganti spasi tengah dengan "_"
    - Menghapus spasi simbol yang tak perlu 
3. Missing value. (Tidak ada missing value dalam dataset original)
4. Merubah tipe data kolom tanggal order dan ship
5. Membuat kolom baru gross_profit_margin dan kolom order_shipping_dur
6. Merubah nama kolo profit menjadi gross_profit
7. Hapus kolom country karena beradapa pada konteks negara US
'''

def clean_data():
    global df
    # 1. Hapus data duplicate
    data_duplicate= df.duplicated().sum()
    if data_duplicate > 0:
        df= df.drop_duplicates()
    
    #2. Normalisasi Kolom:
        ## Semua nama kolom menjadi lowercase
    df.columns = df.columns.str.lower()
        ## Mengganti spasi tengah dengan _
    df.columns = df.columns.str.replace(' ', '_')
        ## Menghapus spasi simbol yang tak perlu 
    df.columns = df.columns.str.replace(r'[^a-zA-Z0-9_]', '')
    
    # 3. Missing Value
    # Tidak ada missing value yang bisa dihandle

    # 4. Merubah tipe data kolom tanggal
    df['order_date']= pd.to_datetime(df['order_date'])
    df['ship_date']= pd.to_datetime(df['ship_date'])
    
    # 5. Membuat kolom baru
    df['gross_profit_margin']= df['profit'] / df['sales']
    df['order_shipping_dur']= df['ship_date'] - df['order_date']
    
    # 6. Merubah nama kolom
    df.rename(columns={'profit': 'gross_profit'}, inplace=True)
    
    # 7. Hapus Kolom country
    df.drop('country', axis= 1, inplace= True)

    # Simpan file mirroring data clean
    df.to_csv('/opt/airflow/dags/P2M3_ahmad_qais_data_clean.csv', index=False)

'''
Fungsi clean_data sudah dibuat
Selanjutnya, saya akan membuat fungsi untuk mengirim data ke elast search
'''

def load_to_elasticsearch():
    # Baca file csv yang sudah dibersihkan
    df= pd.read_csv('/opt/airflow/dags/P2M3_ahmad_qais_data_clean.csv')
    es = Elasticsearch('http://elasticsearch:9200')
    # definisikan nama index di elastic search
    index_name = 'qaisahmad_m3_v2'
    
    # Memuat data ke ElasticSearch
    if es.indices.exists(index=index_name):
        es.delete_by_query(index=index_name, body={"query": {"match_all": {}}})
    else:
        for _, row in df.iterrows():
            es.index(index=index_name, body=row.to_dict()) 
    # Setelah beberapa kali percobaan memuat data ke Elastic search, data sebelumnya masih ada
    # Untuk konteks sekarang, saya cek terlebih dahulu, apabila index exist, saya akan hapus index terlebih dahulu
    # Jika index sudah dipastikan tidak ada, maka data baru ditransfer
    # Cara ini work ditempat saya, namu jika cara ini tidak dibenarka, saya akan menerima masukannya.
            
default_args = {
    'owner': 'qais_ahmad', #MASUKIN NAMA
    'start_date': dt.datetime(2024, 2, 25, 16, 5, 0) - dt.timedelta(hours=7),
    'retries': 1,
    'retry_delay': dt.timedelta(minutes=1),
}

# Definisikan jadwal tugas airflow. Saya menggunakan cron job dimana task akan dilakukan setiap hari pukul 06:30 WIB
with DAG('H8CleanData',
         default_args=default_args,
         schedule_interval= '30 06 * * *', # cara 3 (cron job)
         catchup=False
         ) as dag:
    # Automasi commmand
    clean_data_task = PythonOperator(task_id='clean',
                                     python_callable=clean_data)
    
    load_to_es_task = PythonOperator(task_id='load_to_elasticsearch',
                                     python_callable=load_to_elasticsearch)

clean_data_task >> load_to_es_task