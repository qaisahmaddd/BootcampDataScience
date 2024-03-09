'''
Nama : Ahmad Qais
Batch : RMT - 026
Objecktif : Membuat API sederhana dengan FastAPI dan Exception kalau error. File csv yang digunakan
'Ahmad-Qais.csv' 
http://127.0.0.1:8000
'''

from fastapi import FastAPI, HTTPException
import pandas as pd

app = FastAPI()
@app.get("/") 
def root():
    try :
        df = pd.read_csv("Ahmad_Qais.csv")
        return df.to_dict("records")
    except :
        return HTTPException(status_code=500, detail= "check app")
    

# @app.delete("/")