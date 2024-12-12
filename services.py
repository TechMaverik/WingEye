import os
import cv2
import paths
from zipfile import ZipFile
import numpy as np
from fastapi.responses import FileResponse
from hlengine_ci import HLEngineCoreInspection as Engine


class Services:

    def get_api_version():
        version = {
            "application": "WingEye",
            "api_version": "1.0 Alpha",
            "server": "Development",
        }
        return version

    def detect_rust(images_list):
        PROCESSED_DIR = paths.PROCESSED_DIR
        if not os.path.exists(PROCESSED_DIR):
            os.mkdir(PROCESSED_DIR)

        for single_image in images_list:
            image_full_path = os.path.join(paths.EXTRACTED_DIR, single_image)
            image = Engine.rust_detection(image_full_path)

            new_name = str(image_full_path)
            new_file_name = new_name.replace(paths.EXTRACTED_DIR + "/", " ")
            cv2.imwrite(os.path.join(PROCESSED_DIR, new_file_name), image)

        with ZipFile("_Rust.zip", "w") as zip_object:
            for folder_name, sub_folders, file_names in os.walk(PROCESSED_DIR):
                for filename in file_names:
                    # Create filepath of files in directory
                    file_path = os.path.join(folder_name, filename)
                    # Add files to zip file
                    zip_object.write(file_path, os.path.basename(file_path))

        return FileResponse(
            path="_Rust.zip",
            filename="_Rust.zip",
        )

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
