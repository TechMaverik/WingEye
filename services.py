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

    def delete_temporary_files():
        for folder_name, sub_folders, file_names in os.walk(paths.UPLOAD_DIR):
            for file in file_names:
                full_path = os.path.join(paths.UPLOAD_DIR, file)
                try:
                    os.remove(full_path)
                except:
                    return {"NotFound": paths.UPLOAD_DIR}
        for folder_name, sub_folders, file_names in os.walk(paths.EXTRACTED_DIR):
            for file in file_names:
                full_path = os.path.join(paths.EXTRACTED_DIR, file)
                try:
                    os.remove(full_path)
                except:
                    return {"NotFound": paths.EXTRACTED_DIR}
        for folder_name, sub_folders, file_names in os.walk(paths.PROCESSED_DIR):
            for file in file_names:
                full_path = os.path.join(paths.PROCESSED_DIR, file)
                try:
                    os.remove(full_path)
                except:
                    return {"NotFound": paths.PROCESSED_DIR}
        for folder_name, sub_folders, file_names in os.walk(paths.RESULT_DIR):
            for file in file_names:
                full_path = os.path.join(paths.RESULT_DIR, file)
                try:
                    os.remove(full_path)
                except:
                    return {"NotFound": paths.RESULT_DIR}
        return True

    def detect_rust(images_list):

        for single_image in images_list:
            image_full_path = os.path.join(paths.EXTRACTED_DIR, single_image)
            image = Engine.rust_detection(image_full_path)

            new_name = str(image_full_path)
            new_file_name = new_name.replace(paths.EXTRACTED_DIR + "/", " ")
            cv2.imwrite(os.path.join(paths.PROCESSED_DIR, new_file_name), image)

        zip_full_path = os.path.join(paths.RESULT_DIR, "_Rust.zip")
        with ZipFile(zip_full_path, "w") as zip_object:
            for folder_name, sub_folders, file_names in os.walk(paths.PROCESSED_DIR):
                for filename in file_names:

                    file_path = os.path.join(folder_name, filename)

                    zip_object.write(file_path, os.path.basename(file_path))

        return FileResponse(
            path=zip_full_path,
            filename=zip_full_path,
        )

    def detect_dent(images_list):

        for single_image in images_list:
            image_full_path = os.path.join(paths.EXTRACTED_DIR, single_image)
            image = Engine.dent(image_full_path)

            new_name = str(image_full_path)
            new_file_name = new_name.replace(paths.EXTRACTED_DIR + "/", " ")
            cv2.imwrite(os.path.join(paths.PROCESSED_DIR, new_file_name), image)

        zip_full_path = os.path.join(paths.RESULT_DIR, "_Dent.zip")
        with ZipFile(zip_full_path, "w") as zip_object:
            for folder_name, sub_folders, file_names in os.walk(paths.PROCESSED_DIR):
                for filename in file_names:

                    file_path = os.path.join(folder_name, filename)

                    zip_object.write(file_path, os.path.basename(file_path))

        return FileResponse(
            path=zip_full_path,
            filename=zip_full_path,
        )

    def detect_color_fade(images_list):

        for single_image in images_list:
            image_full_path = os.path.join(paths.EXTRACTED_DIR, single_image)
            image = Engine.color_fade(image_full_path)

            new_name = str(image_full_path)
            new_file_name = new_name.replace(paths.EXTRACTED_DIR + "/", " ")
            cv2.imwrite(os.path.join(paths.PROCESSED_DIR, new_file_name), image)

        zip_full_path = os.path.join(paths.RESULT_DIR, "_Fade.zip")
        with ZipFile(zip_full_path, "w") as zip_object:
            for folder_name, sub_folders, file_names in os.walk(paths.PROCESSED_DIR):
                for filename in file_names:

                    file_path = os.path.join(folder_name, filename)

                    zip_object.write(file_path, os.path.basename(file_path))

        return FileResponse(
            path=zip_full_path,
            filename=zip_full_path,
        )

    def detect_crack(images_list):

        for single_image in images_list:
            image_full_path = os.path.join(paths.EXTRACTED_DIR, single_image)
            image = Engine.crack_detection(image_full_path)

            new_name = str(image_full_path)
            new_file_name = new_name.replace(paths.EXTRACTED_DIR + "/", " ")
            cv2.imwrite(os.path.join(paths.PROCESSED_DIR, new_file_name), image)

        zip_full_path = os.path.join(paths.RESULT_DIR, "_Crack.zip")
        with ZipFile(zip_full_path, "w") as zip_object:
            for folder_name, sub_folders, file_names in os.walk(paths.PROCESSED_DIR):
                for filename in file_names:

                    file_path = os.path.join(folder_name, filename)

                    zip_object.write(file_path, os.path.basename(file_path))

        return FileResponse(
            path=zip_full_path,
            filename=zip_full_path,
        )

    def all_defects_inspection(video_list):

        for single_image in video_list:
            video_full_path = os.path.join(paths.EXTRACTED_DIR, single_image)
            Engine.all_defects_inspection(video_full_path)

        zip_full_path = os.path.join(
            paths.RESULT_DIR, "_All_Defects_Inspection_Video_Result.zip"
        )
        with ZipFile(zip_full_path, "w") as zip_object:
            for folder_name, sub_folders, file_names in os.walk(paths.PROCESSED_DIR):
                for filename in file_names:
                    file_path = os.path.join(folder_name, filename)
                    zip_object.write(file_path, os.path.basename(file_path))

        return FileResponse(
            path=zip_full_path,
            filename=zip_full_path,
        )
