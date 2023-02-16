from typing import Dict


class HttpRequesterSpy:
    """HttpRequester."""

    def __init__(self) -> None:
        """Construct."""
        self.request_from_page_count = 0

    def request_from_page(self) -> Dict[int, str]:
        """Request."""
        self.request_from_page_count += 1
        return {"status_code": 200, "html": "<h1>Something</h1>"}
