
class CitNetError(Exception):
    def __init__(self, message: str = None):
        if message == None:
            message = "An error occured within CitNet."

        super().__init__(message)

class DataError(Exception):
    def __init__(self):
        super().__init__("Unknwon data.")

class AddressError(Exception):
    def __init__(self):
        super().__init__("Please specify address.")