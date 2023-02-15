class ExtractError(Exception):
    """ExtractError."""

    def __init__(self, message: str) -> None:
        """Construct."""
        super().__init__(message)
        self.message = message
        self.error_type = "ExtractError"
