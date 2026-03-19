from functions.level_2.one_pr_url import is_github_pull_request_url


def test__is_github_pull_request_url__True():
    url = "https://github.com/iPoberezhets/typing_challenges/pull/1"
    assert is_github_pull_request_url(url) is True


def test__is_github_pull_request_url__False():
    url = "https://github.com/iPoberezhets/typing_challenges/pull"
    assert is_github_pull_request_url(url) is False


def test__is_github_pull_request_url__not_github():
    url = "https://gitlab.com/iPoberezhets/typing_challenges/pull"
    assert is_github_pull_request_url(url) is False


def test__is_github_pull_request_url__not_pull():
    url = "https://github.com/iPoberezhets/typing_challenges/actions/new"
    assert is_github_pull_request_url(url) is False
