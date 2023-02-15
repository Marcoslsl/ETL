class TranformError(Exception):
    """TranformError."""

    def __init__(self, message) -> None:
        """Construct."""
        super().__init__(message)
        self.message = message
        self.error = "TransformError"
