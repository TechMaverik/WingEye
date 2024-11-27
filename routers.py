import uvicorn
from fastapi import FastAPI, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from handlers import Handlers as wingeye_handlers
import os

SAVE_FOLDER_PATH="Uploaded Image"
if not os.path.exists(SAVE_FOLDER_PATH):
            os.mkdir(SAVE_FOLDER_PATH)

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


@wingeye.post("/rust_detection")
async def rust_detection(input_file: list[UploadFile] | None = None):
    if not input_file:
        return {"message": "No upload file sent"}
    else:
        for file in input_file:
            file_location = f"{SAVE_FOLDER_PATH}/{file.filename}"
            with open(file_location, "wb+") as file_object:
                file_object.write(file.file.read())
            rest_detect=wingeye_handlers.rust_detection(file_location)
            rest_detect
        return

if __name__ == "__main__":
    uvicorn.run(wingeye, host="localhost", port=2024)