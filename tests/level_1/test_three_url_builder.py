from functions.level_1.three_url_builder import build_url
import pytest


@pytest.mark.parametrize(
        "url, host, relative, params",
        [("https://www.youtube.com/watch",
          "https://www.youtube.com",
          "watch",
          None),
         ("https://www.youtube.com/watch?v=bvhr8M7NdTQ&list=RDbvhr8M7NdTQ&start_radio=1&t=3612s",
          "https://www.youtube.com", "watch",
          {"v": "bvhr8M7NdTQ", "list": "RDbvhr8M7NdTQ", "start_radio": "1", "t": "3612s"})]
)
def test__build_url__cases(url, host, relative, params):
    assert build_url(host, relative, params) == url
