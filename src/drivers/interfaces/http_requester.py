from abc import ABC, abstractmethod
from typing import Dict


class HttpRequesterInterface(ABC):
    """HttpRequester Interface."""

    @abstractmethod
    def request_from_page(self) -> Dict[int, str]:
        """Must implement."""
        raise NotImplementedError("Abstract method not implemented.")
