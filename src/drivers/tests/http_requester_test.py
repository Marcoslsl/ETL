from src.drivers.http_requester import HttpRequester


def test_request_from_page():
    """Test."""
    http = HttpRequester()
    r = http.request_from_page()
    print(r)
