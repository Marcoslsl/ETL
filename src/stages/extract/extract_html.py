from datetime import date
from src.drivers.interfaces import HttpRequesterInterface
from src.drivers.interfaces import HtmlCollectorInterface
from src.stages.contracts.extract_contract import ExtractContract
from src.erros import ExtractError


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

    def extract(self) -> ExtractContract:
        """Extract."""
        try:
            html_info = self.__http_requester.request_from_page()
            html = html_info["html"]
            infos = self.__html_collector.collect_essential_information(html)
            return ExtractContract(
                raw_information_content=infos, extraction_date=date.today()
            )
        except Exception as e:
            raise ExtractError(str(e)) from e
