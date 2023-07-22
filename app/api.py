"""
Fastapi App 
"""
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.requests import Request

from app.background_tasks import send_email
from app.schema_init import run_sql_script_initialization, create_connection
from app.api_model import SendEmail
from settings import APISettings

config = APISettings()

app = FastAPI()

@app.on_event("startup")
async def startup_event():
    """Initialize the database schema for dramatiq-pg"""
    run_sql_script_initialization(config)

@app.get("/")
async def home() -> JSONResponse:
    """Home endpoint"""
    return {"message": "Hello World"}

@app.post("/send_email")
async def send_email_request(request: SendEmail) -> JSONResponse:
    send_email.send(request.email, request.subject, request.body)
    return {"message": "Email sent"}

@app.delete("/delete_broker_history")
async def delete_broker_history(request: Request) -> JSONResponse:
    """Delete dramatiq-pg broker history which state already done"""
    conn = create_connection(config)
    with conn.cursor() as cur:
        cur.execute("DELETE FROM dramatiq.queue WHERE state = 'done'")
        conn.commit()
    conn.close()
    return {"message": "Broker history deleted"}
