from src.infra import DatabaseRepository, DatabaseConnector
from src.stages.contracts.mocks import transform_contract_mock
import pytest


@pytest.mark.skip(reason="No need to insert data in database")
def test_insert_artist():
    DatabaseConnector.connect()
    database_repo = DatabaseRepository()
    data = transform_contract_mock.load_content[0]
    database_repo.insert_artist(data)
