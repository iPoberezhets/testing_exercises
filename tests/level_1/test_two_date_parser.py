from functions.level_1.two_date_parser import compose_datetime_from
from datetime import datetime 
import pytest


@pytest.mark.parametrize(
        "date_str, time_str, answer",
        [("",
          "15:16",
          datetime(datetime.today().year,
                   datetime.today().month,
                   datetime.today().day,
                   15, 16)),
         ("tomorrow",
          "15:16",
          datetime(datetime.today().year,
                   datetime.today().month,
                   datetime.today().day+1,
                   15, 16))]
)
def test__compose_datetime_from__today(date_str, time_str, answer):
    assert compose_datetime_from(date_str, time_str) == answer
