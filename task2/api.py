import os
import psycopg2
from fastapi import FastAPI, HTTPException

app = FastAPI()

DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")


def get_db_connection():
    return psycopg2.connect(
        host=DB_HOST,
        port=DB_PORT,
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        connect_timeout=3,
    )


@app.get("/")
def root():
    return {"message": "TEST"}


@app.get("/healthz")
def healthz():
    try:
        conn = get_db_connection()
        conn.close()
        return {"status": "ok"}
    except Exception as e:
        raise HTTPException(status_code=500, detail="DB connection failed")
