class ErrorResponseModel(Exception):
    def __init__(self, code, message):
        self.code = code
        self.message = message

    def to_dict(self):
        return {
            "code": self.code,
            "message": self.message
        }