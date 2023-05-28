class MessageException(Exception):
    def __init__(self, message: str = None, cause: str = None) -> None:
        super().__init__(message)
        self.cause = cause
