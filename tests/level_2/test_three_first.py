from functions.level_2.three_first import first
import pytest


def test__first__first_elem():
    test_data = [1, 2, 3]

    assert first(test_data) == test_data[0]


def test__first__str():
    test_data = '123'

    assert first(test_data) == test_data[0]


def test__first__custom():
    custom_default = "custom"
    assert first(None, custom_default) == custom_default


def test__first__None():
    with pytest.raises(AttributeError):
        first(None)
