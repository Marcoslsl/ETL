from src.stages.extract import ExtractHtml
from src.drivers.html_collector import HtmlCollector
from src.drivers.http_requester import HttpRequester


def test_extract():
    """Test extract."""
    htmlCollector = HtmlCollector()
    httpRequester = HttpRequester()

    ext_html = ExtractHtml(httpRequester, htmlCollector)
    response = ext_html.extract()
    assert isinstance(response, list)
