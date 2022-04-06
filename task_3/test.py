import pytest
from author import long_heavy

TEST_DATA = [(1, {1: 2}), (2, {1: 2, 2: 4}), (3, {1: 2, 2: 4, 3: 6})]


@pytest.mark.parametrize("input_, expected", TEST_DATA)
def test_caching(input_, expected):
    long_heavy(input_)
    actual_result = long_heavy.__closure__[0].cell_contents
    assert (
        actual_result.__closure__[0].cell_contents == expected
    ), " Функция не кэширует"


@pytest.mark.parametrize("input_, expected", [(1, 2), (2, 4), (3, 6)])
def test_function_multiplication(input_, expected):
    assert (
        long_heavy(input_) == expected
    ), f"Функция считает не правильно ожидалось: {expected}, водные данные {input_}"
