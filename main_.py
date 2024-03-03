from fastapi import FastAPI
from database_manager import DatabaseManager
from config import config


app = FastAPI()
db = DatabaseManager(config)


@app.get("/")
def read_root():
    return {"message": "we are alive"}


@app.get("/get_sectors/")
def read_item():
    return {"names": [x[1] for x in db.get_sectors()]}


@app.get("/get_resources/{sector}")
def read_item(sector: str):
    return {"names": [x[1] for x in db.get_resources(sector)]}
