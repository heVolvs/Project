from pydoc import ModuleScanner
from fastapi import FastAPI,File, UploadFile
import logging
import steganography as st
from fastapi.responses import FileResponse
import sqlite3
import db
#Logging parameters

logging.basicConfig(filename='Stegano.log', filemode='w',
 format='%(asctime)s - "Encrypt" -  %(levelname)s - %(message)s',
  datefmt='%d-%m-%y %H:%M:%S',
  level= logging.INFO)

# Database connect
db_con = sqlite3.connect('db.sqlite',check_same_thread=False)

# Intialiasing the API
app = FastAPI()
#-----------------------------------------------------------------------------------

@app.post("/Encrypt/",name = "Encrypt image")
async def create_upload_file(data, uploaded_file: UploadFile = File(...)):
    """Upload a image and a text to be encrypted onto the said image.
 It should return a URL with the encrypted image.
 The image can be any format (JPEG/JPG/PNG/TIF).
 The image cannot be smaller in px than the message encrypted.
 """

    file_location = f"{uploaded_file.filename}"
    with open(file_location, "wb+") as file_object:
        file_object.write(uploaded_file.file.read())
    st.encode(data,uploaded_file.filename)
    logging.info("Image encoded!")
    return FileResponse('stegano2.png') 

#-----------------------------------------------------------------------------------
    
    
@app.post("/Decrypt/", name = "Decrypt image")
async def create_upload_file(uploaded_file2: UploadFile = File(...)):
    """Upload a image that was encrypted in order to decrypt that image.
    The upload format should be .jpg as .png is not supported by FastAPI"""
    file_location = f"{uploaded_file2.filename}"
    with open(file_location, "wb+") as file_object:
        file_object.write(uploaded_file2.file.read())
    logging.info("Image Decoded!")
    return st.decode(uploaded_file2.filename)

#-----------------------------------------------------------------------------------
@app.get("/metrics", name = "Metrics -- WORK IN PROGRESS")

def get_metrics():
    """This doesn't work yet as my database is not working with this app at the moment"""
    return db.get_entries(db_con)
    