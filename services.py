import cv2
import numpy as np
import os

class Services:

    def get_api_version():
        version = {
            "application": "WingEye",
            "api_version": "1.0 Alpha",
            "server": "Development",
        }
        return version
    
    def detect_rust_with_boxes(image_path):
    
        #set output path
        outpath="output"
        if not os.path.exists(outpath):
            os.mkdir(outpath)

        
        # Load the image
        image = cv2.imread(image_path)
        if image is None:
            raise ValueError("Image not found or could not be loaded.")

        # Convert the image to HSV color space
        hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

        # Define color range for rust (adjust these values if necessary)
        lower_rust = np.array([10, 100, 20])    # Lower bound for rust color in HSV
        upper_rust = np.array([30, 255, 200])   # Upper bound for rust color in HSV

        # Create a mask to detect rust color
        rust_mask = cv2.inRange(hsv_image, lower_rust, upper_rust)

        # Find contours in the rust mask
        contours, _ = cv2.findContours(rust_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # Draw bounding boxes around detected rust areas
        for contour in contours:
            # Get the bounding box coordinates for each contour
            x, y, w, h = cv2.boundingRect(contour)
            side = max(w, h)
            square_x, square_y = x + (w - side) // 2, y + (h - side) // 2
            
            # Draw the bounding box on the original image
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 10)  # Red color box with thickness 2
            cv2.putText(image,"*", (square_x, square_y - 50), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)

        
        #Output the image to specified directory
        new_name=str(image_path)
        output_name=new_name.replace("Uploaded Image/"," ")
        result=cv2.imwrite(os.path.join(outpath , f'{output_name}'),image)

        return(result)