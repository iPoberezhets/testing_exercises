from functions.level_2.three_first import first
import pytest


@pytest.mark.parametrize(
        "data, custom,res",
        [
            ([1, 2, 3], None, 1),
            ('123', None, '1'),
            (None, "custom", "custom")
        ]
)
def test__first__first_elem(data, custom, res):
    assert first(data, custom) == res


def test__first__None():
    with pytest.raises(AttributeError):
        first(None)
