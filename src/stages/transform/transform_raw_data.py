from typing import List, Dict
from src.stages.contracts import ExtractContract
from src.stages.contracts import TransformContract
from src.erros import TranformError


class TransformRawData:
    """Transform class."""

    def __init__(self) -> None:
        """Construct."""
        pass

    def transform(
        self, extract_contract: ExtractContract
    ) -> TransformContract:
        """Transform data."""
        try:
            data = self.__filter_and_transform_data(extract_contract)
            data = TransformContract(load_content=data)
        except Exception as e:
            raise TranformError(str(e)) from e

        return data

    def __filter_and_transform_data(
        self, extract_contract: ExtractContract
    ) -> List[Dict]:
        """Tranform data."""
        extraction_date = extract_contract.extraction_date
        data_content = extract_contract.raw_information_content

        transformed_information = []

        for data in data_content:
            transformed_data = None
            link = data["link"]
            if "artistid=" not in link:
                continue

            name = None
            if ", " in data["name"]:
                name = data["name"].split(", ")
            elif " " in data["name"]:
                name = data["name"].split(" ")
            else:
                name = data["name"]

            transformed_data = self.__transform_data(name=name, link=link)
            transformed_data["extraction_data"] = extraction_date
            transformed_information.append(transformed_data)

        return transformed_information

    @classmethod
    def __transform_data(cls, name: List, link: str) -> Dict:
        link_splited = link.split("artistid=")

        second_name = None
        surname = None

        match name:
            case 2:
                first_name = name[1]
                second_name = name[0]
            case 3:
                first_name = name[2]
                second_name = name[0]
                surname = name[1]
            case _:
                first_name = name[0]

        return {
            "first_name": first_name,
            "second_name": second_name,
            "surname": surname,
            "artist_id": link_splited[1],
            "link": link,
        }
