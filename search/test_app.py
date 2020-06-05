"""Tests"""
from datetime import datetime
from pytz import timezone

from search.doc_app import Article


def init_test_data():
    """Prepare objects"""
    date3may = datetime(2020, 5, 3, 23, 59, 59)
    zero_timezone = timezone("Etc/UTC")
    warsaw_timezone = timezone("Europe/Warsaw")
    zero_localized_date3may = zero_timezone.localize(date3may)
    warsaw_localized_date3may = warsaw_timezone.localize(date3may)
    zero_string3may = "2020-05-03T23:59:59Z"
    warsaw_zero_string3may = "2020-05-03T23:59:59+02:00"

    test_article_one = Article(
        meta={"id": 1},
        title="""
Titleone one
        """,
        body="""
Id: 1;
Title: Titleone one;
Published_from_time: 00
        """,
        published_from=zero_localized_date3may,
        tags=["g1", "g2"],
    )

    test_article_two = Article(
        meta={"id": 2},
        title="""
Titletwo two
        """,
        body="""
Id: 2;
Title: Titletwo two;
Published_from_time: +01
        """,
        published_from=warsaw_localized_date3may,
        tags=["g1", "g2"],
    )

    return {
        "articleone": test_article_one,
        "articletwo": test_article_two,
        "timezero": zero_string3may,
        "timewarsaw": warsaw_zero_string3may,
    }


def test_article():
    """Tests if the props ​​are correct"""
    title = """Titleone one"""
    body = """
        Id: 1;\nTitle: Titleone one;\nPublished_from_time: 00
    """.strip()

    data = init_test_data()
    aone = data.get("articleone").to_dict(include_meta=True)
    atwo = data.get("articletwo").to_dict(include_meta=True)
    assert aone["_id"] == 1
    assert aone["_source"]["title"] == title
    assert aone["_source"]["body"] == body
    assert aone["_source"]["published_from"] == data.get("timezero")
    assert atwo["_source"]["published_from"] == data.get("timewarsaw")
    assert atwo["_source"]["tags"][-1] == "g2"
    assert atwo["_source"]["lines"] == 3


def test_is_published():
    """Tests if article is published"""
    data = init_test_data()
    is_published = data.get("articletwo").is_published()
    assert is_published


def test_article_save(mock_client):
    """Tests article saving"""
    data = init_test_data()
    data.get("articletwo").save(using="mock")
    assert mock_client.method_calls[0][2] == {
        "body": {
            "body": "Id: 2;\nTitle: Titletwo two;\nPublished_from_time: +01",
            "lines": 3,
            "published_from": "2020-05-03T23:59:59+02:00",
            "tags": ["g1", "g2"],
            "title": "Titletwo two",
        },
        "id": 2,
        "index": "blog",
    }
