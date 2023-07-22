"""
PostgreSQL database schema initialization for dramatiq-pg
"""
import os
from psycopg2 import connect
from dramatiq_pg import generate_init_sql
from settings import APISettings

def create_connection(config:APISettings):
    """
    Creates a connection to the database.
    """
    return connect(
        host=config.POSTGRES_HOST,
        port=config.POSTGRES_PORT,
        user=config.POSTGRES_USER,
        password=config.POSTGRES_PASSWORD,
        database=config.POSTGRES_DB,
    )

def run_sql_script_initialization(config:APISettings):
    """
    Runs a SQL script to initialize the database schema.
    """
    sql_script = generate_init_sql()
    print("Initializing dramatic-pg schema")
    with create_connection(config) as conn:
        with conn.cursor() as cur:
            try:
                cur.execute(sql_script)
                conn.commit()
                print("dramatic-pg schema initialized")
            except Exception as e:
                conn.rollback()
                print("dramatic-pg schema already exists")
            
