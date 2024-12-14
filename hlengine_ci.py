import os
import cv2
import paths
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
            # cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 10)
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

    def all_defects_inspection(video_path):

        video = cv2.VideoCapture(video_path)
        if not video.isOpened():
            return {"error": "Cannot open video file"}

        new_name = str(video_path)
        new_file_name = new_name.replace(paths.EXTRACTED_DIR + "/", " ")

        result_video_full_path = os.path.join(paths.PROCESSED_DIR, new_file_name)

        fps = int(video.get(cv2.CAP_PROP_FPS))
        frame_width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
        frame_height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
        fourcc = cv2.VideoWriter_fourcc(*"mp4v")
        output_video_path = result_video_full_path
        output_video = cv2.VideoWriter(
            output_video_path, fourcc, fps, (frame_width, frame_height)
        )

        while True:
            ret, frame = video.read()
            if not ret:
                break
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            edges = cv2.Canny(gray, 50, 150)
            frame[edges > 150] = [255, 0, 0]
            output_video.write(frame)
        video.release()
        output_video.release()

    def detect_rust_from_video(video_path):

        video = cv2.VideoCapture(video_path)
        if not video.isOpened():
            return {"error": "Cannot open video file"}

        new_name = str(video_path)
        new_file_name = new_name.replace(paths.EXTRACTED_DIR + "/", " ")

        result_video_full_path = os.path.join(paths.PROCESSED_DIR, new_file_name)

        fps = int(video.get(cv2.CAP_PROP_FPS))
        frame_width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
        frame_height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
        fourcc = cv2.VideoWriter_fourcc(*"mp4v")
        output_video_path = result_video_full_path
        output_video = cv2.VideoWriter(
            output_video_path, fourcc, fps, (frame_width, frame_height)
        )

        while True:
            ret, frame = video.read()
            if not ret:
                break

            lab = cv2.cvtColor(frame, cv2.COLOR_BGR2LAB)
            l_channel, a_channel, b_channel = cv2.split(lab)

            lower_rust = np.array([80, 130, 100])  # Lower bound for rust color
            upper_rust = np.array([150, 160, 140])  # Upper bound for rust color

            rust_mask = cv2.inRange(lab, lower_rust, upper_rust)

            kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (7, 7))
            rust_mask = cv2.morphologyEx(rust_mask, cv2.MORPH_CLOSE, kernel)

            contours, _ = cv2.findContours(
                rust_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
            )

            # Draw bounding boxes around the detected rust areas
            for contour in contours:
                if cv2.contourArea(contour) > 0:
                    x, y, w, h = cv2.boundingRect(contour)
                    side = max(w, h)
                    square_x, square_y = x + (w - side) // 2, y + (h - side) // 2
                    cv2.putText(
                        frame,
                        "*",
                        (square_x, square_y - 50),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.8,
                        (0, 0, 255),
                        2,
                    )

            output_video.write(frame)
        video.release()
        output_video.release()
