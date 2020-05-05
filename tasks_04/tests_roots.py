from tasks_04.quadratic_equation_roots import find_roots


def test_two_roots():
    equation = '1x^2+2x-3=0'
    expected = (1.0, -3.0)
    actual = find_roots(equation)

    assert len(actual) == 2
    assert sorted(expected) == sorted(actual)