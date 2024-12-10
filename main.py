# import package 
# fastapi
from fastapi import FastAPI, HTTPException, Header
import pandas as pd

# membuat instance/object FastAPI
app = FastAPI()

# membuat API key
api_key = "secret123"

# tokopedia.com/ -> halaman utama

# rules
# endpoint -> url yang akan digunakan oleh client
# HTTP function (get, put, post, delete)
# alamat url

# define endpoint -> endpoint home
@app.get("/")
def getData(kunci: str = Header(None)): # tambahan proteksi api key
    # do some process

    # validate kunci:
    # cek ketersediaan kunci dalam request
    # cek kesamaan value kunci dengan api key
    if kunci == None or kunci != api_key:
        # jika kunci tidak ada / kunci != api key
        # return error
        raise HTTPException(status_code=401, detail="Anda tidak punya akses ke endpoint ini")

    # return hasil process (berupa dict/json)
    return {
        "message": "selamat datang!"
    }

@app.get("/data")
def getDataCsv():
    # retrieve data existing from source
    df = pd.read_csv("data.csv")

    # do some process

    # sebelum return, convert DataFrame to dictionary
    # return hasil process (berupa dict/json)
    return df.to_dict(orient="records")

# endpoint untuk mencari nama dari source
@app.get("/data/{name}")
def getFilterData(name: str):
    # retrieve data existing from source
    df = pd.read_csv("data.csv")

    # do some process
    # logic filter data
    filter = df[df['nama'] == name]
    
    # validasi -> jika kosong -> error -> error 500
    if len(filter) == 0:
        # error handling
        # return/raise exception -> HTTP Exception
        raise HTTPException(status_code=500, detail="Data tidak ditemukan")

    # sebelum return, convert DataFrame to dictionary
    # return hasil process (berupa dict/json)
    return filter.to_dict(orient="records")


# menjalankan script di terminal
# uvicorn [nama_file]:[nama_instance] --reload
# uvicorn main:app --reload

# --reload -> fitur auto-refresh ketika ada code change

# shortcut untuk mematikan uvicorn
# ctrl + c

# localhost atau 127.0.0.1 -> alamat default ketika menjalankan uvicorn di komputer sendiri (local)
# :8000 -> nomor port default dari uvicorn

# pengujian api
# browser -> hanya untuk http function get
# documentation -> 
# - sebagai informasi/buku manual dari API yang sudah dibuat
# - tempat menguji api -> bisa untuk semua http function

# fastapi -> include docs -> Swagger -> akses: endpoint /docs
# opsi: install Postman -> software API documentation

# url ->
# ada dynamic parameter/url parameter

# step preparation sebelum deployment
# 1. setup repository github
# 2. memenuhi beberapa file
#       - requirements.txt
#       - vercel.json
#       - package.json

