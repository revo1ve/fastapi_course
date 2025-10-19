import uvicorn
from fastapi import FastAPI

from app.config import load_config
from app.logger import logger


app = FastAPI()
config = load_config()

app.debug = config.debug


@app.get("/")
def read_root():
    logger.info("Handling request to root endpoint")
    return {"message": "Hello, World!"}


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)


@app.get("/db")
def get_db_info():
    logger.info(f"Connecting to database: {config.db.database_url}")
    return {"database_url": config.db.database_url}
