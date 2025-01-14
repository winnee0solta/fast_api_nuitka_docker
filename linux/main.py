import logging
logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s")

from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def read_root():
    logging.debug("Processing root endpoint.")
    return {"Hello": "World"}

if __name__ == "__main__":
    import uvicorn
    logging.debug("Starting FastAPI application.")
    uvicorn.run(app, host="0.0.0.0", port=8000, log_level="debug")
