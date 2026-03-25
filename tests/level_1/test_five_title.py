from functions.level_1.five_title import change_copy_item
import pytest


def test__change_copy_item__simple_title():
    test_title = "test_title"
    assert change_copy_item(test_title) == "Copy of test_title"


def test__change_copy_item__big_title():
    big_title = "test"*100
    assert change_copy_item(big_title) == "test"*100


def test__change_copy_item__copy_of_copy():
    copy_title = "Copy of test"
    assert change_copy_item(copy_title) == "Copy of test (2)"


def test__change_copy_item__copy_of_copy_2():
    copy_title = "Copy of test (2)"
    assert change_copy_item(copy_title) == "Copy of test (3)"


def test__change_copy_item__copy_of_copy_with_brackets():
    copy_title = "Copy of test (NAN)"
    assert change_copy_item(copy_title) == "Copy of test (NAN) (2)"


def test__change_copy_item__copy_of_copy_with_brackets_2():
    copy_title = "Copy of test (NAN) (2)"
    assert change_copy_item(copy_title) == "Copy of test (NAN) (3)"


def test__change_copy_item__wrong_type():
    with pytest.raises(AttributeError):
        change_copy_item(10)
