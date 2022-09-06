from fastapi import FastAPI,File, UploadFile
import logging
import steganography as st
from fastapi.responses import FileResponse
import sqlite3
from endb import create_entry
#Logging parameters
logging.basicConfig(filename='Stegano.log', filemode='w',
 format='%(asctime)s - "Encrypt" -  %(levelname)s - %(message)s',
  datefmt='%d-%m-%y %H:%M:%S',
  level= logging.INFO)

db_con = sqlite3.connect('db.sqlite')

# Intialiasing the API
app = FastAPI()


@app.post("/Encrypt/")

async def create_upload_file(data, uploaded_file: UploadFile = File(...)):
    """Upload a image and a text to be encrypted onto the said image.
 It should return a URL with the encrypted image."""

    file_location = f"{uploaded_file.filename}"
    with open(file_location, "wb+") as file_object:
        file_object.write(uploaded_file.file.read())
    st.encode(data,uploaded_file.filename)
    return FileResponse('stegano2.png') 
    
    
@app.post("/Decrypt/")
async def create_upload_file(uploaded_file2: UploadFile = File(...)):
    """Upload a image that was encrypted in order to decrypt that image.
    The upload format should be .jpg as .png is not supported by FastAPI"""
    file_location = f"{uploaded_file2.filename}"
    with open(file_location, "wb+") as file_object:
        file_object.write(uploaded_file2.file.read())
    return st.decode(uploaded_file2.filename)

    