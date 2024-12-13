import os
import paths
import zipfile
from fastapi import File
from fastapi.responses import JSONResponse
from services import Services as wingeye_services


class Handlers:

    def get_api_version():
        version = wingeye_services.get_api_version()
        return version

    def unzip_files(self, zip_path):
        if not os.path.exists(zip_path):
            return JSONResponse(status_code=404, content={"message": "File not found"})
        with zipfile.ZipFile(zip_path, "r") as zip_ref:
            zip_ref.extractall(paths.EXTRACTED_DIR)
        return True

    def detect_rust(self, zip_path):
        status = self.unzip_files(zip_path)
        extracted_images_list = []
        for image in os.listdir(paths.EXTRACTED_DIR):
            extracted_images_list.append(image)
        response = wingeye_services.detect_rust(extracted_images_list)
        return response

    def dent_detection(self, zip_path):
        status = self.unzip_files(zip_path)
        extracted_images_list = []
        for image in os.listdir(paths.EXTRACTED_DIR):
            extracted_images_list.append(image)
        response = wingeye_services.detect_dent(extracted_images_list)
        return response

    def detect_color_fade(self, zip_path):
        status = self.unzip_files(zip_path)
        extracted_images_list = []
        for image in os.listdir(paths.EXTRACTED_DIR):
            extracted_images_list.append(image)
        response = wingeye_services.detect_color_fade(extracted_images_list)
        return response

    def detect_crack(self, zip_path):
        status = self.unzip_files(zip_path)
        extracted_images_list = []
        for image in os.listdir(paths.EXTRACTED_DIR):
            extracted_images_list.append(image)
        response = wingeye_services.detect_crack(extracted_images_list)
        return response
