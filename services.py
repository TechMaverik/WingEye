import os
import cv2
import paths
import numpy as np
from fastapi.responses import FileResponse


class Services:

    def get_api_version():
        version = {
            "application": "WingEye",
            "api_version": "1.0 Alpha",
            "server": "Development",
        }
        return version

    def detect_rust_with_boxes(image_path):

        PROCESSED_DIR = paths.PROCESSED_DIR
        if not os.path.exists(PROCESSED_DIR):
            os.mkdir(PROCESSED_DIR)

        image = cv2.imread(image_path)
        if image is None:
            raise ValueError("Image not found or could not be loaded.")

        hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

        lower_rust = np.array([10, 100, 20])  # Lower bound for rust color in HSV
        upper_rust = np.array([30, 255, 200])  # Upper bound for rust color in HSV

        rust_mask = cv2.inRange(hsv_image, lower_rust, upper_rust)

        contours, _ = cv2.findContours(
            rust_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
        )

        for contour in contours:

            x, y, w, h = cv2.boundingRect(contour)
            side = max(w, h)
            square_x, square_y = x + (w - side) // 2, y + (h - side) // 2

            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 10)
            cv2.putText(
                image,
                "*",
                (square_x, square_y - 50),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.8,
                (0, 0, 255),
                2,
            )

        new_name = str(image_path)
        new_file_name = new_name.replace(paths.UPLOAD_DIR + "/", " ")
        cv2.imwrite(os.path.join(PROCESSED_DIR, new_file_name), image)

        file_path = os.path.join(PROCESSED_DIR, new_file_name)
        print(file_path)
        if os.path.exists(file_path):
            return FileResponse(path=file_path, filename=file_path)
        return {"error": "File not found"}
