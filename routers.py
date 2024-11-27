import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from handlers import Handlers as wingeye_handlers


wingeye=FastAPI()
wingeye.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@wingeye.get("/")
def get_api_version():
    version = wingeye_handlers.get_api_version()
    return version



if __name__ == "__main__":
    uvicorn.run(wingeye, host="localhost", port=2024)