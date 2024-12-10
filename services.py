import os
import cv2
import paths
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

    def detect_rust(image_path):

        PROCESSED_DIR = paths.PROCESSED_DIR
        if not os.path.exists(PROCESSED_DIR):
            os.mkdir(PROCESSED_DIR)

        image = Engine.rust_detection(image_path)
        new_name = str(image_path)
        new_file_name = new_name.replace(paths.UPLOAD_DIR + "/", " ")
        cv2.imwrite(os.path.join(PROCESSED_DIR, new_file_name), image)

        file_path = os.path.join(PROCESSED_DIR, new_file_name)
        print(file_path)
        if os.path.exists(file_path):
            return FileResponse(path=file_path, filename=file_path)
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
