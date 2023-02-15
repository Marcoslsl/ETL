from src.stages.extract import ExtractHtml
from src.drivers.html_collector import HtmlCollector
from src.drivers.tests.spy_http_requester import HttpRequesterSpy
from src.drivers.tests.spy_html_collector import HtmlCollectorSpy
from src.stages.contracts.extract_contract import ExtractContract
from src.erros.extract_error import ExtractError


def test_extract():
    """Test extract."""
    htmlCollector = HtmlCollectorSpy()
    httpRequester = HttpRequesterSpy()

    ext_html = ExtractHtml(httpRequester, htmlCollector)
    response = ext_html.extract()
    assert isinstance(response, ExtractContract)
    assert httpRequester.request_from_page_count == 1
    assert "html" in htmlCollector.collector


def test_extract_error():
    """Test extract error.
    it must be an error
    """
    htmlCollector = HtmlCollectorSpy()
    httpRequester = "Error"

    ext_html = ExtractHtml(httpRequester, htmlCollector)

    try:
        response = ext_html.extract()
    except Exception as e:
        assert isinstance(e, ExtractError)
