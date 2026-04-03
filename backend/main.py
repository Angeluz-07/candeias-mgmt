from fastapi import FastAPI
from entrypoints.api import router

app = FastAPI(title="Candeias Management API", version="0.0.1")

app.include_router(router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)