""" 
Dramatiq background tasks
"""
from time import sleep
import dramatiq
from settings import APISettings
from dramatiq_pg import PostgresBroker, generate_init_sql

config = APISettings()

broker = PostgresBroker(
    url=f"postgres://{config.POSTGRES_USER}:{config.POSTGRES_PASSWORD}@{config.POSTGRES_HOST}:{config.POSTGRES_PORT}/{config.POSTGRES_DB}",
    results=True,
)

dramatiq.set_broker(broker)

@dramatiq.actor(store_results=True)
def send_email(email, subject, body):
    print(f"Sending email to {email} with subject {subject} and body {body}")
    sleep(5)
    print("Email sent")
    return f"Email sent to {email} with subject {subject} and body {body}"