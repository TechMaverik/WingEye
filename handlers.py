from services import Services as wingeye_services

class Handlers:

    def get_api_version():
        version=wingeye_services.get_api_version()
        return version