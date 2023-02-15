from src.stages.extract import ExtractHtml
from src.drivers.html_collector import HtmlCollector
from src.drivers.http_requester import HttpRequester
from src.stages.contracts.extract_contract import ExtractContract
from src.erros.extract_error import ExtractError


def test_extract():
    """Test extract."""
    htmlCollector = HtmlCollector()
    httpRequester = HttpRequester()

    ext_html = ExtractHtml(httpRequester, htmlCollector)
    response = ext_html.extract()
    assert isinstance(response, ExtractContract)


def test_extract_error():
    """Test extract error.
    it must be an error
    """
    htmlCollector = HtmlCollector()
    httpRequester = "Error"

    ext_html = ExtractHtml(httpRequester, htmlCollector)

    try:
        response = ext_html.extract()
    except Exception as e:
        assert isinstance(e, ExtractError)
