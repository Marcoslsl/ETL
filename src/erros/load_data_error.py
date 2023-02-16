class LoadError(Exception):
    """LoadError."""

    def __init__(self, message: str) -> None:
        """Construct."""
        super().__init__(message)
        self.message = message
        self.error_type = "LoadError"
