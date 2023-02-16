from src.stages.transform import TransformRawData
from src.stages.contracts.mocks import extract_contract_mock
from src.stages.contracts import TransformContract
from src.erros import TranformError


def test_TransformRawData():
    t_raw_data = TransformRawData()
    t_raw_data = t_raw_data.transform(extract_contract_mock)
    assert isinstance(t_raw_data, TransformContract)
    assert "first_name" in t_raw_data.load_content[0]
    assert "artist_id" in t_raw_data.load_content[0]
    assert "link" in t_raw_data.load_content[0]
    assert "extraction_data" in t_raw_data.load_content[0]


def test_TransformRawData_error():
    t_raw_data = TransformRawData()
    try:
        t_raw_data.transform("SomethingToRaiseError")
    except Exception as e:
        assert isinstance(e, TranformError)
