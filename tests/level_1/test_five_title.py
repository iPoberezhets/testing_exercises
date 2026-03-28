from functions.level_1.five_title import change_copy_item
import pytest


@pytest.mark.parametrize(
        "title, result",
        [("test_title", "Copy of test_title"),
         ("test"*100, "test"*100),
         ("Copy of test", "Copy of test (2)"),
         ("Copy of test (2)", "Copy of test (3)"),
         ("Copy of test (NAN)", "Copy of test (NAN) (2)"),
         ("Copy of test (NAN) (2)", "Copy of test (NAN) (3)")
         ]
)
def test__change_copy_item__check_titles(title, result):
    assert change_copy_item(title) == result


def test__change_copy_item__wrong_type():
    with pytest.raises(AttributeError):
        change_copy_item(10)
