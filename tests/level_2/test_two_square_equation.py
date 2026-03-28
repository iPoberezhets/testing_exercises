from functions.level_2.two_square_equation import solve_square_equation
import pytest


@pytest.mark.parametrize(
        "coefs, res",
        [
            ((1.0, 1.0, 10.0), (None, None)),
            ((0.0, 0.0, 4.0), (None, None)),
            ((0.0, 4.0, 4.0), (-1.0, None)),
            ((1.0, 4.0, 4.0), (-2.0, -2.0)),
            ((1.0, 1.0, -6.0), (-3, 2))
        ]
)
def test__solve_square_equation(coefs, res):
    assert solve_square_equation(*coefs) == res
