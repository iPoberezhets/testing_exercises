from functions.level_2.two_square_equation import solve_square_equation


def test__solve_square_equation__negative_discriminant():
    a, b, c = 1.0, 1.0, 10.0

    assert solve_square_equation(a, b, c) == (None, None)


def test__solve_square_equation__zero_roots():
    a, b, c = 0.0, 0.0, 4.0

    assert solve_square_equation(a, b, c) == (None, None)


def test__solve_square_equation__one_roots():
    a, b, c = 0.0, 4.0, 4.0

    assert solve_square_equation(a, b, c) == (-1.0, None)


def test__solve_square_equation__two_equal_roots():
    a, b, c = 1.0, 4.0, 4.0

    assert solve_square_equation(a, b, c) == (-2.0, -2.0)


def test__solve_square_equation__two_roots():
    a, b, c = 1.0, 1.0, -6.0

    assert solve_square_equation(a, b, c) == (-3, 2)

