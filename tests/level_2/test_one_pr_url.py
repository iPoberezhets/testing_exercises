from functions.level_2.one_pr_url import is_github_pull_request_url
import pytest


@pytest.mark.parametrize(
        "url, res",
        [
         ("https://github.com/iPoberezhets/typing_challenges/pull/1", True),
         ("https://github.com/iPoberezhets/typing_challenges/pull", False),
         ("https://gitlab.com/iPoberezhets/typing_challenges/pull", False),
         ("https://github.com/iPoberezhets/typing_challenges/actions/new", False),
        ]
)
def test__is_github_pull_request_url(url, res):
    assert is_github_pull_request_url(url) is res
