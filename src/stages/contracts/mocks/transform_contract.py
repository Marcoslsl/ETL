import datetime
from src.stages.contracts import TransformContract


transform_contract_mock = TransformContract(
    load_content=[
        {
            "first_name": "Zanini",
            "second_name": None,
            "surname": None,
            "artist_id": "11597",
            "link": "https://web.archive.org/web/20121007172955/http://www.nga.gov/cgi-bin/tsearch?artistid=11597",
            "extraction_data": datetime.date(2023, 2, 15),
        },
        {
            "first_name": "Zanini-Viola",
            "second_name": None,
            "surname": None,
            "artist_id": "11597",
            "link": "https://web.archive.org/web/20121007172955/http://www.nga.gov/cgi-bin/tsearch?artistid=11597",
            "extraction_data": datetime.date(2023, 2, 15),
        },
        {
            "first_name": "Zanotti",
            "second_name": None,
            "surname": None,
            "artist_id": "11631",
            "link": "https://web.archive.org/web/20121007172955/http://www.nga.gov/cgi-bin/tsearch?artistid=11631",
            "extraction_data": datetime.date(2023, 2, 15),
        },
        {
            "first_name": "Zao",
            "second_name": None,
            "surname": None,
            "artist_id": "3427",
            "link": "https://web.archive.org/web/20121007172955/http://www.nga.gov/cgi-bin/tsearch?artistid=3427",
            "extraction_data": datetime.date(2023, 2, 15),
        },
    ]
)
