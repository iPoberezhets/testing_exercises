from functions.level_1.three_url_builder import build_url


def test__build_url_no_params():
    url = "https://www.youtube.com/watch"
    host_name = "https://www.youtube.com"
    relative_url = "watch"
    assert build_url(host_name, relative_url) == url


def test__build_url__with_params():
    url = "https://www.youtube.com/watch?v=bvhr8M7NdTQ&list=RDbvhr8M7NdTQ&start_radio=1&t=3612s"  # топ альбом
    host_name = "https://www.youtube.com"
    relative_url = "watch"
    get_params = {"v": "bvhr8M7NdTQ", "list": "RDbvhr8M7NdTQ", "start_radio": "1", "t": "3612s"}
    assert build_url(host_name, relative_url, get_params) == url
