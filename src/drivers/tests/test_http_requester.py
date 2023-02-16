from src.drivers import HttpRequester


def test_request_from_page(requests_mock):
    """Test."""
    url = (
        "https://web.archive.org/web/20121007172955/http:"
        "//www.nga.gov/collection/anZ1.htm"
    )
    response_context = "<h1>HelloWorld</h1>"
    requests_mock.get(url, status_code=200, text=response_context)

    http = HttpRequester()
    r = http.request_from_page()
    assert "status_code" in r
    assert "html" in r
    assert r["status_code"] == 200
    assert r["html"] == response_context
