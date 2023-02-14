from typing import Dict
import requests


class HttpRequester:
    """HttpRequester."""

    def __init__(self) -> None:
        """Construct."""
        self.__url = (
            "https://web.archive.org/web/20121007172955/http:"
            "//www.nga.gov/collection/anZ1.htm"
        )

    def request_from_page(self) -> Dict[int, str]:
        """Request."""
        response = requests.get(self.__url)
        return {"status_code": response.status_code, "html": response.text}
