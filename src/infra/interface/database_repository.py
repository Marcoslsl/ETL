from typing import Dict
from abc import ABC, abstractmethod


class DatabaseRepositoryInterface(ABC):
    """DatabaseRepositoryInterface."""

    @abstractmethod
    def insert_artist(cls, data: Dict) -> None:
        """Must implement."""
        raise NotImplementedError("Abstract method not implemented.")
