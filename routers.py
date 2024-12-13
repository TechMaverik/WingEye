import os
import uvicorn
import paths
from fastapi import FastAPI, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from handlers import Handlers as wingi_handlers


if not os.path.exists(paths.UPLOAD_DIR):
    os.mkdir(paths.UPLOAD_DIR)
if not os.path.exists(paths.PROCESSED_DIR):
    os.mkdir(paths.PROCESSED_DIR)
if not os.path.exists(paths.RESULT_DIR):
    os.mkdir(paths.RESULT_DIR)
if not os.path.exists(paths.EXTRACTED_DIR):
    os.mkdir(paths.EXTRACTED_DIR)

wingi = FastAPI()
wingi.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@wingi.get("/")
def get_api_version():
    version = wingi_handlers.get_api_version()
    return version


@wingi.get("/delete_files")
def delete_files():
    response = wingi_handlers.delete_files()
    return response


@wingi.post("/rust_detection")
async def rust_detection(input_file: list[UploadFile] | None = None):
    if not input_file:
        return {"message": "No upload file sent"}
    else:
        for file in input_file:
            file_location = f"{paths.UPLOAD_DIR}/{file.filename}"
            with open(file_location, "wb+") as file_object:
                file_object.write(file.file.read())
            response = wingi_handlers().detect_rust(file_location)
        return response


@wingi.post("/dent_detection")
async def rust_detection(input_file: list[UploadFile] | None = None):
    if not input_file:
        return {"message": "No upload file sent"}
    else:
        for file in input_file:
            file_location = f"{paths.UPLOAD_DIR}/{file.filename}"
            with open(file_location, "wb+") as file_object:
                file_object.write(file.file.read())
            response = wingi_handlers().dent_detection(file_location)
        return response


# Needs improvemnt
@wingi.post("/color_fade")
async def rust_detection(input_file: list[UploadFile] | None = None):
    if not input_file:
        return {"message": "No upload file sent"}
    else:
        for file in input_file:
            file_location = f"{paths.UPLOAD_DIR}/{file.filename}"
            with open(file_location, "wb+") as file_object:
                file_object.write(file.file.read())
            response = wingi_handlers().detect_color_fade(file_location)
        return response


@wingi.post("/crack")
async def rust_detection(input_file: list[UploadFile] | None = None):
    if not input_file:
        return {"message": "No upload file sent"}
    else:
        for file in input_file:
            file_location = f"{paths.UPLOAD_DIR}/{file.filename}"
            with open(file_location, "wb+") as file_object:
                file_object.write(file.file.read())
            response = wingi_handlers().detect_crack(file_location)
        return response


if __name__ == "__main__":
    uvicorn.run(wingi, host="localhost", port=2024)
