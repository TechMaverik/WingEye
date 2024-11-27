from services import Services as wingeye_services

class Handlers:

    def get_api_version():
        version=wingeye_services.get_api_version()
        return version
    
    def rust_detection(image_path):
        rust=wingeye_services.detect_rust_with_boxes(image_path)
        return rust