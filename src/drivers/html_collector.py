from src.drivers.interfaces import HtmlCollectorInterface
from bs4 import BeautifulSoup as bs
from typing import List, Dict


class HtmlCollector(HtmlCollectorInterface):
    """HtmlCollector."""

    @classmethod
    def collect_essential_information(cls, html: str) -> List[Dict[str, str]]:
        """Collect information.

        Parameters
        ----------
        html: str
            html
        """
        soup = bs(html, "html.parser")

        artist_name_list = soup.find(class_="BodyText")
        artist_name_list_items = artist_name_list.find_all("a")

        essential_information = []
        for artist_name in artist_name_list_items:
            names = artist_name.get_text()
            links = "https://web.archive.org" + artist_name.get("href")
            essential_information.append({"name": names, "link": links})
        return essential_information
