from app import app, config
import uvicorn


if __name__ == "__main__":
    uvicorn.run(app, host=config.API_HOST, port=config.API_PORT)