from services import Services as wingeye_services


class Handlers:

    def get_api_version():
        version = wingeye_services.get_api_version()
        return version

    def rust_detection(image_path):
        response = wingeye_services.detect_rust(image_path)
        return response

    def dent_detection(image_path):
        response = wingeye_services.detect_dent(image_path)
        return response

    def detect_color_fade(image_path):
        response = wingeye_services.detect_color_fade(image_path)
        return response

    def detect_crack(image_path):
        response = wingeye_services.detect_crack(image_path)
        return response
    
    def unzip(file_location):
        response=wingeye_services.unzip_file(file_location)
        return response

    def zip(file_location):
        response=wingeye_services.zip_file(file_location)
        return response
    
    def remove_tempfiles(folder):
        response=wingeye_services.remove_tempfiles(folder)
        return response