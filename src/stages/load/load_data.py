from src.infra.interface import DatabaseRepositoryInterface
from src.stages.contracts import TransformContract
from src.erros import LoadError


class LoadData:
    """LoadData."""

    def __init__(self, repository: DatabaseRepositoryInterface) -> None:
        """Construct."""
        self.__repository = repository

    def load(self, transformed_data_contract: TransformContract) -> None:
        """Load."""
        try:
            load_content = transformed_data_contract.load_content
            for data in load_content:
                self.__repository.insert_artist(data)
        except Exception as e:
            raise LoadError(str(e)) from e
