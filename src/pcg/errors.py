class PCGError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(message)


    def __repr__(self):
        return f'PCGError: {self.message}'


    def __str__(self):
        return f"PCGError: {self.message}"
