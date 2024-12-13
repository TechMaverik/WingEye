import cv2
import numpy as np


class HLEngineCoreInspection:

    def crack_detection(image_path):
        image = cv2.imread(image_path)
        if image is None:
            return {"Error": "Image not Found"}
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        edges = cv2.Canny(gray, threshold1=50, threshold2=150)
        featured_image = image.copy()
        featured_image[edges > 0] = [0, 0, 255]
        return featured_image

    def rust_detection(image_path):
        image = cv2.imread(image_path)
        if image is None:
            return {"Error": "Image not Found"}
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
        return image

    def color_fade(image_path, fade_threshold=100):
        image = cv2.imread(image_path)
        if image is None:
            return {"Error": "Image not Found"}

        hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        h, s, v = cv2.split(hsv_image)
        faded_mask = cv2.inRange(s, 0, fade_threshold)
        featured_image = cv2.bitwise_and(image, image, mask=faded_mask)
        return featured_image

    def dent(image_path):
        image = cv2.imread(image_path)
        if image is None:
            return {"Error": "Image not Found"}
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        thresh = cv2.adaptiveThreshold(
            gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 2
        )
        thresh_cleaned = cv2.morphologyEx(
            cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, np.ones((5, 5), np.uint8)),
            cv2.MORPH_OPEN,
            np.ones((5, 5), np.uint8),
        )
        contours, _ = cv2.findContours(
            thresh_cleaned, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
        )
        for contour in sorted(contours, key=cv2.contourArea, reverse=True):
            area = cv2.contourArea(contour)
            if area > 50:  # Minimum area threshold
                x, y, w, h = cv2.boundingRect(contour)
                side = max(w, h)
                square_x, square_y = x + (w - side) // 2, y + (h - side) // 2
                # cv2.rectangle(image, (square_x, square_y), (square_x + side, square_y + side), (0, 0, 255), 2)
                cv2.putText(
                    image,
                    "*",
                    (square_x, square_y - 50),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.8,
                    (255, 0, 0),
                    10,
                )
        return image
