import os
import uvicorn
import paths
from fastapi import FastAPI, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from handlers import Handlers as wingeye_handlers


if not os.path.exists(paths.UPLOAD_DIR):
    os.mkdir(paths.UPLOAD_DIR)
if not os.path.exists(paths.PROCESSED_DIR):
    os.mkdir(paths.PROCESSED_DIR)
if not os.path.exists(paths.RESULT_DIR):
    os.mkdir(paths.RESULT_DIR)
if not os.path.exists(paths.EXTRACTED_DIR):
    os.mkdir(paths.EXTRACTED_DIR)

wingeye = FastAPI()
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


@wingeye.get("/delete_files")
def delete_files():
    response = wingeye_handlers.delete_files()
    return response


@wingeye.post("/rust_detection")
async def rust_detection(input_file: list[UploadFile] | None = None):
    if not input_file:
        return {"message": "No upload file sent"}
    else:
        for file in input_file:
            file_location = f"{paths.UPLOAD_DIR}/{file.filename}"
            with open(file_location, "wb+") as file_object:
                file_object.write(file.file.read())
            response = wingeye_handlers().detect_rust(file_location)
        return response


@wingeye.post("/dent_detection")
async def rust_detection(input_file: list[UploadFile] | None = None):
    if not input_file:
        return {"message": "No upload file sent"}
    else:
        for file in input_file:
            file_location = f"{paths.UPLOAD_DIR}/{file.filename}"
            with open(file_location, "wb+") as file_object:
                file_object.write(file.file.read())
            response = wingeye_handlers().dent_detection(file_location)
        return response


# Needs improvemnt
@wingeye.post("/color_fade")
async def rust_detection(input_file: list[UploadFile] | None = None):
    if not input_file:
        return {"message": "No upload file sent"}
    else:
        for file in input_file:
            file_location = f"{paths.UPLOAD_DIR}/{file.filename}"
            with open(file_location, "wb+") as file_object:
                file_object.write(file.file.read())
            response = wingeye_handlers().detect_color_fade(file_location)
        return response


@wingeye.post("/crack")
async def rust_detection(input_file: list[UploadFile] | None = None):
    if not input_file:
        return {"message": "No upload file sent"}
    else:
        for file in input_file:
            file_location = f"{paths.UPLOAD_DIR}/{file.filename}"
            with open(file_location, "wb+") as file_object:
                file_object.write(file.file.read())
            response = wingeye_handlers().detect_crack(file_location)
        return response


if __name__ == "__main__":
    uvicorn.run(wingeye, host="localhost", port=2024)
