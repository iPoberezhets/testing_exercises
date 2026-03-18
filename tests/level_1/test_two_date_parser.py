from functions.level_1.two_date_parser import compose_datetime_from
from datetime import datetime 


def test__compose_datetime_from__today():
    date_str = ""
    time_str = "15:16"
    answer = datetime(datetime.today().year,
                      datetime.today().month,
                      datetime.today().day,
                      15,
                      16)

    assert compose_datetime_from(date_str, time_str) == answer


def test__compose_datetime_from__tomorrow():
    date_str = "tomorrow"
    time_str = "15:16"
    answer = datetime(datetime.today().year,
                      datetime.today().month,
                      datetime.today().day+1,
                      15,
                      16)

    assert compose_datetime_from(date_str, time_str) == answer
