from typing import List, Dict


class HtmlCollectorSpy:
    """HtmlCollector."""

    def __init__(self) -> None:
        """Construct."""
        self.collector = {}

    def collect_essential_information(self, html: str) -> List[Dict[str, str]]:
        """Collect information."""
        self.collector["html"] = html
        list_ = [{"name": "SomeName", "link": "https://something.com"}]
        return list_
