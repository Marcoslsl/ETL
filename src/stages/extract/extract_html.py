from src.drivers.interfaces import HttpRequesterInterface
from src.drivers.interfaces import HtmlCollectorInterface


class ExtractHtml:
    """Extrac Html."""

    def __init__(
        self,
        http_requester: HttpRequesterInterface,
        html_collector: HtmlCollectorInterface,
    ) -> None:
        """Construct."""
        self.__http_requester = http_requester
        self.__html_collector = html_collector

    def extract(self):
        """Extract."""
        html_info = self.__http_requester.request_from_page()
        html = html_info["html"]
        infos = self.__html_collector.collect_essential_information(html)
        return infos
