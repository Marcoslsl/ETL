from src.stages import ExtractHtml, TransformRawData, LoadData
from src.drivers import HtmlCollector, HttpRequester
from src.infra.database_connector import DatabaseConnector
from src.infra.database_repository import DatabaseRepository


class MainPipeline:
    """Main Pipeline."""

    def __init__(self) -> None:
        """Construct."""
        self.__extract_html = ExtractHtml(HttpRequester(), HtmlCollector())
        self.__transform_raw_data = TransformRawData()
        self.__load_data = LoadData(DatabaseRepository())

    def run_pipeline(self) -> None:
        """Run the ETL pipeline."""
        DatabaseConnector.connect()
        extract = self.__extract_html.extract()
        transform = self.__transform_raw_data.transform(extract)
        load = self.__load_data.load(transform)
