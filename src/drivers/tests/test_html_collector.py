from src.drivers.html_collector import HtmlCollector
from src.drivers.mocks.http_requester_mock import mock_request_from_page
from random import randint


def test_collect_essential_information():
    html = mock_request_from_page()
    html = html["html"]

    html_collector = HtmlCollector()
    information = html_collector.collect_essential_information(html)

    random_position = randint(1, 32)
    assert isinstance(information, list)
    assert isinstance(information[random_position], dict)
    assert "name" in information[random_position]
    assert "link" in information[random_position]
