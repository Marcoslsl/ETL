from src.stages.contracts.mocks import transform_contract_mock
from src.stages.load import LoadData
from src.erros import LoadError


class RepositorySpy:
    def __init__(self) -> None:
        self.insert_artists_atributes = []

    def insert_artist(self, data):
        self.insert_artists_atributes.append(data)


def test_load():
    repo = RepositorySpy()
    load_data = LoadData(repo)
    mock = transform_contract_mock
    load_data.load(mock)
    assert repo.insert_artists_atributes == mock.load_content


def test_load_error():
    repo = RepositorySpy()
    load_data = LoadData(repo)
    mock = transform_contract_mock
    try:
        load_data.load("SomethingToRaiseError")
    except Exception as e:
        assert isinstance(e, LoadError)
