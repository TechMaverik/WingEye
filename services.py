import os
import cv2
import paths
import pathlib
import numpy as np
from fastapi.responses import FileResponse
from hlengine_ci import HLEngineCoreInspection as Engine
from zipfile import ZipFile

UPLOAD_TO_DIR = paths.UPLOAD_DIR
PROCESSED_DIR = paths.PROCESSED_DIR

class Services:

    # def __init__(self):
    #     self.Engine = HLEngineCoreInspection()

    def get_api_version():
        version = {
            "application": "WingEye",
            "api_version": "1.0 Alpha",
            "server": "Development",
        }
        return version

    def detect_rust(image_path):

        
        if not os.path.exists(PROCESSED_DIR):
            os.mkdir(PROCESSED_DIR)


        image = Engine.rust_detection(image_path)
        new_name = str(image_path)
        new_file_name = new_name.replace(paths.UPLOAD_DIR + "/", " ")
        cv2.imwrite(os.path.join(PROCESSED_DIR, new_file_name), image)

        file_path = os.path.join(PROCESSED_DIR, new_file_name)
        
        if os.path.exists(file_path):
            return file_path
        return {"error": "File not found"}

    def detect_dent(image_path):

        PROCESSED_DIR = paths.PROCESSED_DIR
        if not os.path.exists(PROCESSED_DIR):
            os.mkdir(PROCESSED_DIR)

        image = Engine.dent(image_path)
        new_name = str(image_path)
        new_file_name = new_name.replace(paths.UPLOAD_DIR + "/", " ")
        cv2.imwrite(os.path.join(PROCESSED_DIR, new_file_name), image)

        file_path = os.path.join(PROCESSED_DIR, new_file_name)
        print(file_path)
        if os.path.exists(file_path):
            return FileResponse(path=file_path, filename=file_path)
        return {"error": "File not found"}

    def detect_color_fade(image_path):

        PROCESSED_DIR = paths.PROCESSED_DIR
        if not os.path.exists(PROCESSED_DIR):
            os.mkdir(PROCESSED_DIR)

        image = Engine.color_fade(image_path)
        new_name = str(image_path)
        new_file_name = new_name.replace(paths.UPLOAD_DIR + "/", " ")
        cv2.imwrite(os.path.join(PROCESSED_DIR, new_file_name), image)

        file_path = os.path.join(PROCESSED_DIR, new_file_name)
        print(file_path)
        if os.path.exists(file_path):
            return FileResponse(path=file_path, filename=file_path)
        return {"error": "File not found"}

    def detect_crack(image_path):

        PROCESSED_DIR = paths.PROCESSED_DIR
        if not os.path.exists(PROCESSED_DIR):
            os.mkdir(PROCESSED_DIR)

        image = Engine.crack_detection(image_path)
        new_name = str(image_path)
        new_file_name = new_name.replace(paths.UPLOAD_DIR + "/", " ")
        cv2.imwrite(os.path.join(PROCESSED_DIR, new_file_name), image)

        file_path = os.path.join(PROCESSED_DIR, new_file_name)
        print(file_path)
        if os.path.exists(file_path):
            return FileResponse(path=file_path, filename=file_path)
        return {"error": "File not found"}

    def unzip_file(file_location):
        zipped_files=ZipFile(file_location)
        zipped_files.extractall(UPLOAD_TO_DIR)
        ZipFile.close(zipped_files)
        os.remove(file_location)
        return
    
    def zip_file(file_location):
        output_file=f"{PROCESSED_DIR}/Output.zip"
        file_to_zip=os.path.basename(file_location)
        with ZipFile(output_file, mode='a') as archive:
            archive.write(file_location, file_to_zip)
        return
    
    def remove_tempfiles(folder):
        files=os.listdir(f"{folder}")
        for current_file in files:
            to_delete=os.path.join(folder,current_file)
            file_type=pathlib.Path(to_delete).suffix
            if file_type!= ".zip":
                os.remove(to_delete)
        return